from typing import TypedDict

import pytest

from lowdb.low import Low
from lowdb.adapters.memory import Memory


class ObjType(TypedDict):
    a: int
    b: str


@pytest.mark.asyncio
async def test_low():
    low = Low[ObjType](Memory())

    assert low.data is None

    obj: ObjType = {
        "a": 123,
        "b": "foo",
    }

    low.data = obj

    await low.write()

    await low.read()

    assert low.data == obj
