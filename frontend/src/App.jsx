import { useState, useEffect } from 'react'
import { getTodos, createTodo, updateTodo, deleteTodo } from './api'
import { TodoInput } from './components/TodoInput'
import { TodoItem } from './components/TodoItem'
import './index.css'

function App() {
  const [todos, setTodos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchTodos()
  }, [])

  const fetchTodos = async () => {
    try {
      const data = await getTodos()
      setTodos(data)
      setError(null)
    } catch (err) {
      setError('Failed to load todos')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleAdd = async (title) => {
    try {
      const newTodo = await createTodo({ title, completed: false })
      setTodos([...todos, newTodo])
    } catch (err) {
      console.error('Failed to create todo:', err)
    }
  }

  const handleToggle = async (id, completed) => {
    try {
      const updated = await updateTodo(id, { completed })
      setTodos(todos.map(t => t.id === id ? updated : t))
    } catch (err) {
      console.error('Failed to update todo:', err)
    }
  }

  const handleDelete = async (id) => {
    try {
      await deleteTodo(id)
      setTodos(todos.filter(t => t.id !== id))
    } catch (err) {
      console.error('Failed to delete todo:', err)
    }
  }

  return (
    <div className="h-screen flex items-center justify-center">
      <div className="max-w-md w-full mx-auto rounded-lg shadow-md bg-blue-600 p-6">
        <h1 className="text-2xl font-bold tracking-tight text-white">
          Todo<span className="text-gray-500">App</span>
        </h1>

        <TodoInput onAdd={handleAdd} />

        {loading && <div className="py-4 text-center text-gray-300">Loading tasks...</div>}
        {error && <div className="py-4 text-center text-red-500">{error}</div>}
        {todos.length === 0 && !loading && !error && <div className="py-4 text-center text-gray-300">No tasks yet. Add one above!</div>}

        <ul className="mt-4 space-y-3">
          {!loading && !error && todos.map(todo => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggle={handleToggle}
              onDelete={handleDelete}
            />
          ))}
        </ul>
      </div>
    </div>
  )
}

export default App
