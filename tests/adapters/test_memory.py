from typing import TypedDict

import pytest

from lowdb.adapters.memory import Memory


class ObjType(TypedDict):
    a: int
    b: str


@pytest.mark.asyncio
async def test_memory():
    mem = Memory[ObjType]()

    assert await mem.read() == None

    obj: ObjType = {
        "a": 123,
        "b": "foo",
    }

    await mem.write(obj)

    assert await mem.read() == obj
