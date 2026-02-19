from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI Items API - Starter")


class Item(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None


# Simple in-memory storage
_items: List[Item] = []
_next_id = 1


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in _items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _next_id += 1
    _items.append(item)
    return item


# Example initial data
_items.append(Item(id=1, name="Example Item", description="A starter example"))
_next_id = 2
