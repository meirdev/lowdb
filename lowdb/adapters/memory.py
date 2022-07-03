from typing import Optional

from ..low import Adapter, T


class Memory(Adapter[T]):
    def __init__(self) -> None:
        super().__init__()

        self._data: Optional[T] = None

    async def read(self) -> Optional[T]:
        return self._data

    async def write(self, data: Optional[T]) -> None:
        self._data = data
