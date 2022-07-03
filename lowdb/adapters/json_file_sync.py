import json
from typing import Optional

from ..low_sync import Adapter, T


class JSONFile(Adapter[T]):
    def __init__(self, filename: str) -> None:
        super().__init__()

        self._filename = filename

    def read(self) -> Optional[T]:
        try:
            with open(self._filename) as fp:
                return json.load(fp)
        except FileNotFoundError:
            return None

    def write(self, data: Optional[T]) -> None:
        with open(self._filename, "w") as fp:
            json.dump(data, fp)
