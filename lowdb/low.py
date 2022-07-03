from abc import ABCMeta, abstractmethod
from typing import Generic, Optional, TypeVar


T = TypeVar("T")


class Adapter(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    async def read(self) -> Optional[T]:
        pass

    @abstractmethod
    async def write(self, data: Optional[T]) -> None:
        pass


class Low(Generic[T]):
    def __init__(self, adapter: Adapter[T]) -> None:
        self._adapter = adapter

        self._data: Optional[T] = None

    @property
    def data(self) -> Optional[T]:
        return self._data

    @data.setter
    def data(self, data: Optional[T]) -> None:
        self._data = data

    async def read(self) -> None:
        self._data = await self._adapter.read()

    async def write(self) -> None:
        await self._adapter.write(self._data)
