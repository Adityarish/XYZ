# crud.py
from db import db
from models import TodoInDB, TodoCreate, TodoUpdate
from typing import List
from bson import ObjectId

async def create_todo(todo: TodoCreate) -> dict:
    doc = todo.model_dump()
    result = await db.todos.insert_one(doc)
    doc["_id"] = result.inserted_id
    return TodoInDB(**doc).model_dump()

async def get_todos() -> List[dict]:
    cursor = db.todos.find().sort("_id", -1)
    return [TodoInDB(**doc).model_dump() async for doc in cursor]

async def get_todo(todo_id: str):
    doc = await db.todos.find_one({"_id": ObjectId(todo_id)})
    return TodoInDB(**doc).model_dump() if doc else None

async def update_todo(todo_id: str, todo: TodoUpdate):
    update = {k: v for k, v in todo.model_dump().items() if v is not None}
    if not update:
        return await get_todo(todo_id)
    await db.todos.update_one({"_id": ObjectId(todo_id)}, {"$set": update})
    return await get_todo(todo_id)

async def delete_todo(todo_id: str):
    res = await db.todos.delete_one({"_id": ObjectId(todo_id)})
    return res.deleted_count == 1
