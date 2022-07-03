from typing import Optional

from ..low_sync import Adapter, T


class Memory(Adapter[T]):
    def __init__(self) -> None:
        super().__init__()

        self._data: Optional[T] = None

    def read(self) -> Optional[T]:
        return self._data

    def write(self, data: Optional[T]) -> None:
        self._data = data
