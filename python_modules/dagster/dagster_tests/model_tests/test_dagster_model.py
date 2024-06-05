from typing import Optional

import pytest
from dagster._check import CheckError
from dagster._model import DagsterModel, copy, dagster_model, dagster_model_with_new
from dagster._model.decorator import SerdesOptions
from dagster._serdes.serdes import deserialize_value, serialize_value
from dagster._utils.cached_method import CACHED_METHOD_CACHE_FIELD, cached_method
from pydantic import ValidationError


def test_runtime_typecheck() -> None:
    class MyClass(DagsterModel):
        foo: str
        bar: int

    with pytest.raises(ValidationError):
        MyClass(foo="fdsjk", bar="fdslk")  # type: ignore # good job type checker

    @dagster_model
    class MyClass2:
        foo: str
        bar: int

    with pytest.raises(CheckError):
        MyClass2(foo="fdsjk", bar="fdslk")  # type: ignore # good job type checker


def test_override_constructor_in_subclass() -> None:
    class MyClass(DagsterModel):
        foo: str
        bar: int

        def __init__(self, foo: str, bar: int):
            super().__init__(foo=foo, bar=bar)

    assert MyClass(foo="fdsjk", bar=4)

    @dagster_model
    class MyClass2:
        foo: str
        bar: int

        def __new__(cls, foo: str, bar: int):
            return super().__new__(
                cls,
                foo=foo,  # type: ignore
                bar=bar,  # type: ignore
            )

    assert MyClass2(foo="fdsjk", bar=4)


def test_override_constructor_in_subclass_different_arg_names() -> None:
    class MyClass(DagsterModel):
        foo: str
        bar: int

        def __init__(self, fooarg: str, bararg: int):
            super().__init__(foo=fooarg, bar=bararg)

    assert MyClass(fooarg="fdsjk", bararg=4)

    @dagster_model_with_new
    class MyClass2:
        foo: str
        bar: int

        def __new__(cls, fooarg: str, bararg: int):
            return super().__new__(
                cls,
                foo=fooarg,  # type: ignore
                bar=bararg,  # type: ignore
            )

    assert MyClass2(fooarg="fdsjk", bararg=4)


def test_override_constructor_in_subclass_wrong_type() -> None:
    class MyClass(DagsterModel):
        foo: str
        bar: int

        def __init__(self, foo: str, bar: str):
            super().__init__(foo=foo, bar=bar)

    with pytest.raises(ValidationError):
        MyClass(foo="fdsjk", bar="fdslk")

    @dagster_model_with_new
    class MyClass2:
        foo: str
        bar: int

        def __new__(cls, foo: str, bar: str):
            return super().__new__(cls, foo=foo, bar=bar)  # type: ignore

    with pytest.raises(CheckError):
        MyClass2(foo="fdsjk", bar="fdslk")


def test_model_copy() -> None:
    class MyClass(DagsterModel):
        foo: str
        bar: int

    obj = MyClass(foo="abc", bar=5)
    assert obj.model_copy(update=dict(foo="xyz")) == MyClass(foo="xyz", bar=5)
    assert obj.model_copy(update=dict(bar=6)) == MyClass(foo="abc", bar=6)
    assert obj.model_copy(update=dict(foo="xyz", bar=6)) == MyClass(foo="xyz", bar=6)

    @dagster_model
    class MyClass2:
        foo: str
        bar: int

    obj = MyClass2(foo="abc", bar=5)

    assert copy(obj, foo="xyz") == MyClass2(foo="xyz", bar=5)
    assert copy(obj, bar=6) == MyClass2(foo="abc", bar=6)
    assert copy(obj, foo="xyz", bar=6) == MyClass2(foo="xyz", bar=6)


def test_non_model_param():
    class SomeClass: ...

    class OtherClass: ...

    class MyModel(DagsterModel):
        some_class: SomeClass

    assert MyModel(some_class=SomeClass())

    with pytest.raises(ValidationError):
        MyModel(some_class=OtherClass())  # wrong class

    with pytest.raises(ValidationError):
        MyModel(some_class=SomeClass)  # forgot ()

    @dagster_model
    class MyModel2:
        some_class: SomeClass

    assert MyModel2(some_class=SomeClass())

    with pytest.raises(CheckError):
        MyModel2(some_class=OtherClass())  # wrong class

    with pytest.raises(CheckError):
        MyModel2(some_class=SomeClass)  # forgot ()


def test_cached_method() -> None:
    class CoolModel(DagsterModel):
        name: str

        @cached_method
        def calculate(self, n: int):
            return {self.name: n}

        @cached_method
        def reticulate(self, n: int):
            return {self.name: n}

    m = CoolModel(name="bob")
    assert m.calculate(4) is m.calculate(4)
    assert m.calculate(4) is not m.reticulate(4)

    assert CACHED_METHOD_CACHE_FIELD not in m.dict()

    @dagster_model(enable_cached_method=True)
    class CoolModel2:
        name: str

        @cached_method
        def calculate(self, n: int):
            return {self.name: n}

        @cached_method
        def reticulate(self, n: int):
            return {self.name: n}

        @property
        @cached_method
        def prop(self):
            return {"four": 4}

    m = CoolModel2(name="bob")
    assert m.calculate(4) is m.calculate(4)
    assert m.calculate(4) is not m.reticulate(4)
    assert m.prop is m.prop

    clean_m = CoolModel2(name="bob")
    # cache doesn't effect equality
    assert clean_m == m
    assert m == clean_m

    # cache doesn't effect hash
    s = {m, clean_m}
    assert len(s) == 1

    # cache erased on copy
    m_copy = copy(m)
    assert m_copy.calculate(4) is not m.calculate(4)


def test_forward_ref() -> None:
    @dagster_model
    class Parent:
        partner: Optional["Parent"]
        child: Optional["Child"]

    class Child: ...

    assert Parent(partner=None, child=None)


def test_forward_ref_with_new() -> None:
    @dagster_model_with_new
    class Parent:
        partner: Optional["Parent"]
        child: Optional["Child"]

        def __new__(cls, partner=None, child=None):
            return super().__new__(
                cls,
                partner=partner,
                child=child,
            )

    class Child: ...

    assert Parent()


def test_serdes() -> None:
    @dagster_model(serdes=True)
    class SerializeTest:
        name: str
        age: int

    obj = SerializeTest(name="Lyra", age=2)
    assert obj == deserialize_value(serialize_value(obj))

    stored_name = "TheHiddenTruth"

    @dagster_model(serdes=SerdesOptions(storage_name=stored_name))
    class SerializeArgsTest:
        name: str
        age: int

    obj = SerializeArgsTest(name="Lyra", age=2)
    obj_str = serialize_value(obj)
    assert stored_name in obj_str
    assert obj == deserialize_value(obj_str)
