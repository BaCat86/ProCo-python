from fastapi import FastAPI
from pydantic import BaseModel
import database as db

app = FastAPI()

# Define a request model
class Item(BaseModel):
    name: str
    price: float

# An in-memory database
def main():
    db.create()

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"item_id": item_id, "item": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id in items_db:
        return {"item_id": item_id, "item": items_db[item_id]}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return {"message": "Item deleted"}
    return {"error": "Item not found"}

if __name__ == "__main__":
    main()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
