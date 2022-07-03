import tempfile
from typing import TypedDict

from lowdb.adapters.json_file_sync import JSONFile


class ObjType(TypedDict):
    a: int
    b: str


def test_json_file():
    with tempfile.NamedTemporaryFile("w+") as fp:
        json_file = JSONFile[ObjType](fp.name)

        obj: ObjType = {
            "a": 123,
            "b": "foo",
        }

        json_file.write(obj)

        assert json_file.read() == obj
