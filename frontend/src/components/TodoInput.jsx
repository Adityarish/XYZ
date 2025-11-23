import { useState } from 'react'

export function TodoInput({ onAdd }) {
    const [text, setText] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault()
        if (text.trim()) {
            onAdd(text)
            setText('')
        }
    }

    return (
        <form onSubmit={handleSubmit} className="w-full flex gap-4">
            <input
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Add a new task..."
                className="flex-1 bg-transparent border-b-2 border-white/20 py-2 px-4 text-white placeholder-white/40 focus:outline-none focus:border-white transition-colors text-lg"
            />
            <button
                type="submit"
                disabled={!text.trim()}
                className="px-6 py-2 bg-white text-black font-bold rounded-full hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
            >
                Add
            </button>
        </form>
    )
}
