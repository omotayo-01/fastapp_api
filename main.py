from fastapi import FastAPI, Query
from fastapi import FastAPI

app = FastAPI()

# Fake database
items = {
    1: {"name": "Book", "price": 10},
    2: {"name": "Pen", "price": 2}
}

# 1. GET - Read items
@app.get("/items")
def get_items():
    return items

# 2. POST - Create item
@app.post("/items")
def create_item(item_id: int, name: str, price: float):
    items[item_id] = {"name": name, "price": price}
    return {"message": "Item created", "item": items[item_id]}

# 3. PUT - Update item
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    if item_id not in items:
        return {"error": "Item not found"}
    
    items[item_id] = {"name": name, "price": price}
    return {"message": "Item updated", "item": items[item_id]}

# 4. DELETE - Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}
    
    deleted = items.pop(item_id)
    return {"message": "Item deleted", "item": deleted}
#5. from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
#6. from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

7.# Pydantic model for JSON body
class Item(BaseModel):
    name: str
    price: float

8.# Sample data
items = {
    1: {"name": "Book", "price": 10},
    2: {"name": "Pen", "price": 2}
}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

9.# Get all items
@app.get("/items")
def get_items():
    return items

10.# Add or update an item using JSON body
@app.post("/items")
def update_item(item_id: int = Query(...), item: Item = ...):
    items[item_id] = item.dict()
=======
from fastapi import FastAPI, Query
from fastapi import FastAPI

app = FastAPI()

# Fake database
items = {
    1: {"name": "Book", "price": 10},
    2: {"name": "Pen", "price": 2}
}

# 1. GET - Read items
@app.get("/items")
def get_items():
    return items

# 2. POST - Create item
@app.post("/items")
def create_item(item_id: int, name: str, price: float):
    items[item_id] = {"name": name, "price": price}
    return {"message": "Item created", "item": items[item_id]}

# 3. PUT - Update item
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    if item_id not in items:
        return {"error": "Item not found"}
    
    items[item_id] = {"name": name, "price": price}
    return {"message": "Item updated", "item": items[item_id]}

# 4. DELETE - Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}
    
    deleted = items.pop(item_id)
    return {"message": "Item deleted", "item": deleted}
#5. from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
#6. from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

7.# Pydantic model for JSON body
class Item(BaseModel):
    name: str
    price: float

8.# Sample data
items = {
    1: {"name": "Book", "price": 10},
    2: {"name": "Pen", "price": 2}
}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

9.# Get all items
@app.get("/items")
def get_items():
    return items

10.# Add or update an item using JSON body
@app.post("/items")
def update_item(item_id: int = Query(...), item: Item = ...):
    items[item_id] = item.dict()
    return items[item_id]