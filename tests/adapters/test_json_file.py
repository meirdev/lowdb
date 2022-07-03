import tempfile
from typing import TypedDict

import pytest

from lowdb.adapters.json_file import JSONFile


class ObjType(TypedDict):
    a: int
    b: str


@pytest.mark.asyncio
async def test_json_file():
    with tempfile.NamedTemporaryFile("w+") as fp:
        json_file = JSONFile[ObjType](fp.name)

        obj: ObjType = {
            "a": 123,
            "b": "foo",
        }

        await json_file.write(obj)

        assert await json_file.read() == obj
