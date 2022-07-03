from typing import TypedDict

from lowdb.adapters.memory_sync import Memory


class ObjType(TypedDict):
    a: int
    b: str


def test_memory():
    mem = Memory[ObjType]()

    assert mem.read() == None

    obj: ObjType = {
        "a": 123,
        "b": "foo",
    }

    mem.write(obj)

    assert mem.read() == obj
