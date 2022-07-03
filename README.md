# lowdb

Simple to use local JSON database. Inspired by https://github.com/typicode/lowdb

# Usage

```python
import asyncio
from typing import TypedDict

from lowdb.low import Low
from lowdb.adapters.json_file import JSONFile


class Post(TypedDict):
    id: int
    title: str


class Data(TypedDict):
    posts: list[Post]


async def main() -> None:
    db = Low[Data](JSONFile("db.json"))

    await db.read()

    db.data = db.data or {"posts": []}

    db.data["posts"].append({
        "id": 1,
        "title": "lowdb is awesome",
    })

    await db.write()


if __name__ == "__main__":
    asyncio.run(main())
```
