import Database from "better-sqlite3"

const dbName = process.env.DB_NAME ?? "tasks.db"
export const db = new Database(dbName)

// テーブル作成（初回のみ）
db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0
  )
`)
