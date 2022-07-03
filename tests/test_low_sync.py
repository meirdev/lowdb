from typing import TypedDict

from lowdb.low_sync import Low
from lowdb.adapters.memory_sync import Memory


class ObjType(TypedDict):
    a: int
    b: str


def test_low():
    low = Low[ObjType](Memory())

    assert low.data is None

    obj: ObjType = {
        "a": 123,
        "b": "foo",
    }

    low.data = obj

    low.write()

    low.read()

    assert low.data == obj
