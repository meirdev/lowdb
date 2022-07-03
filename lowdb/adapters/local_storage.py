import json
from typing import Optional

from js import localStorage

from ..low import Adapter, T


class LocalStorage(Adapter[T]):
    def __init__(self, key: str) -> None:
        super().__init__()

        self._key = key

    def read(self) -> Optional[T]:
        value = localStorage.getItem(self._key)

        if value is None:
            return value

        return json.loads(value)

    def write(self, data: Optional[T]) -> None:
        localStorage.setItem(self._key, json.dumps(data))
