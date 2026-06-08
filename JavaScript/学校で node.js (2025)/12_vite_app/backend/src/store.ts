import { db } from "./db"
import { Task } from "./types"

type TaskRow = {
  id: number
  title: string
  completed: number
}

export function getTasks(): Task[] {
  const rows = db.prepare("SELECT * FROM tasks").all() as TaskRow[]
  return rows.map((row) => ({
    id: row.id,
    title: row.title,
    completed: Boolean(row.completed)
  }))
}

export function addTask(title: string): Task {
  const stmt = db.prepare("INSERT INTO tasks (title, completed) VALUES (?, ?)")
  const result = stmt.run(title, 0)
  return {
    id: Number(result.lastInsertRowid),
    title,
    completed: false
  }
}

export function updateTask(id: number, completed: boolean): Task | null {
  const stmt = db.prepare("UPDATE tasks SET completed = ? WHERE id = ?")
  const result = stmt.run(completed ? 1 : 0, id)
  if (result.changes === 0) return null
  const row = db.prepare("SELECT * FROM tasks WHERE id = ?").get(id) as TaskRow
  return {
    id: row.id,
    title: row.title,
    completed: Boolean(row.completed)
  }
}

export function deleteTask(id: number): boolean {
  const stmt = db.prepare("DELETE FROM tasks WHERE id = ?")
  const result = stmt.run(id)
  return result.changes > 0
}
