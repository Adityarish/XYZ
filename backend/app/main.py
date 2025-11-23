# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import TodoCreate, TodoUpdate
from crud import create_todo, get_todos, get_todo, update_todo, delete_todo

app = FastAPI(title="Todo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for production restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/todos", status_code=201)
async def api_create_todo(payload: TodoCreate):
    doc = await create_todo(payload)
    return doc

@app.get("/todos")
async def api_get_todos():
    return await get_todos()

@app.get("/todos/{todo_id}")
async def api_get_todo(todo_id: str):
    doc = await get_todo(todo_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    return doc

@app.put("/todos/{todo_id}")
async def api_update_todo(todo_id: str, payload: TodoUpdate):
    doc = await update_todo(todo_id, payload)
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    return doc

@app.delete("/todos/{todo_id}", status_code=204)
async def api_delete_todo(todo_id: str):
    ok = await delete_todo(todo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
