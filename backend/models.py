from pydantic import BaseModel


class ItemID(BaseModel):
    id: list[int] = []