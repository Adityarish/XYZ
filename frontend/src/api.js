const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

async function request(path, opts) {
  const res = await fetch(API_BASE + path, {
    headers: { "Content-Type": "application/json" },
    ...opts,
  });
  if (!res.ok) throw new Error(await res.text());
  if (res.status === 204) return null;
  return res.json();
}

export const getTodos = () => request("/todos");
export const createTodo = (todo) => request("/todos", { method: "POST", body: JSON.stringify(todo) });
export const updateTodo = (id, data) => request(`/todos/${id}`, { method: "PUT", body: JSON.stringify(data) });
export const deleteTodo = (id) => request(`/todos/${id}`, { method: "DELETE" });
