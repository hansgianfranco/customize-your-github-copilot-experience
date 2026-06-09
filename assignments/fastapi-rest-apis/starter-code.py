from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Items API - FastAPI Starter")


class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class ItemOut(Item):
    id: int


# In-memory storage
_items: List[ItemOut] = []
_next_id = 1


@app.get("/")
def read_root():
    return {"message": "FastAPI starter is running"}


@app.get("/items/", response_model=List[ItemOut])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    for it in _items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items/", response_model=ItemOut, status_code=201)
def create_item(item: Item):
    global _next_id
    new = ItemOut(id=_next_id, **item.dict())
    _items.append(new)
    _next_id += 1
    return new


@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item: Item):
    for idx, it in enumerate(_items):
        if it.id == item_id:
            updated = ItemOut(id=item_id, **item.dict())
            _items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, it in enumerate(_items):
        if it.id == item_id:
            _items.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
