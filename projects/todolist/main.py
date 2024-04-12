from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Define a model for the to-do item
class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

# Initialize an empty list to store the to-do items
todo_list: List[TodoItem] = []

# Endpoint to create a new to-do item
@app.post("/todos/", response_model=TodoItem)
async def create_todo_item(todo_item: TodoItem):
    todo_list.append(todo_item)
    return todo_item

# Endpoint to get all to-do items
@app.get("/todos/", response_model=List[TodoItem])
async def get_all_todo_items():
    return todo_list

# Endpoint to get a specific to-do item by its ID
@app.get("/todos/{todo_id}", response_model=TodoItem)
async def get_todo_item(todo_id: int):
    for todo_item in todo_list:
        if todo_item.id == todo_id:
            return todo_item
    raise HTTPException(status_code=404, detail="Todo item not found")

# Endpoint to update a specific to-do item by its ID
@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo_item(todo_id: int, updated_todo: TodoItem):
    for index, todo_item in enumerate(todo_list):
        if todo_item.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo item not found")

# Endpoint to delete a specific to-do item by its ID
@app.delete("/todos/{todo_id}", response_model=dict)
async def delete_todo_item(todo_id: int):
    for index, todo_item in enumerate(todo_list):
        if todo_item.id == todo_id:
            del todo_list[index]
            return {"message": "Todo item deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo item not found")
