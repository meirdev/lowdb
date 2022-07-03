import json
from typing import Optional

import aiofiles

from ..low import Adapter, T


class JSONFile(Adapter[T]):
    def __init__(self, filename: str) -> None:
        super().__init__()

        self._filename = filename

    async def read(self) -> Optional[T]:
        try:
            async with aiofiles.open(self._filename) as fp:
                contents = await fp.read()

            return json.loads(contents)
        except FileNotFoundError:
            return None

    async def write(self, data: Optional[T]) -> None:
        contents = json.dumps(data)

        async with aiofiles.open(self._filename, "w") as fp:
            await fp.write(contents)
