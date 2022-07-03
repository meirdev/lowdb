from typing import TypedDict

from lowdb.adapters.local_storage import LocalStorage


class ObjType(TypedDict):
    a: int
    b: str


def test_local_storage():
    local_storage = LocalStorage[ObjType]()

    assert local_storage.read() is None

    obj: ObjType = {
        "a": 123,
        "b": "foo",
    }

    local_storage.write(obj)

    assert local_storage.read() == obj
