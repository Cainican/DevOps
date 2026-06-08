import { Hono } from "hono"
import { serve } from "@hono/node-server"
import { cors } from "hono/cors"
import { getTasks, addTask, updateTask, deleteTask } from "./store"

const app = new Hono()

app.use("*", cors())

app.get("/tasks", (c) => {
  return c.json(getTasks())
})

app.post("/tasks", async (c) => {
  const body = await c.req.json<{ title: string }>()
  const task = addTask(body.title)
  return c.json(task)
})

app.put("/tasks/:id", async (c) => {
  const id = Number(c.req.param("id"))
  const body = await c.req.json<{ completed: boolean }>()
  const task = updateTask(id, body.completed)
  if (!task) return c.json({ error: "Not found" }, 404)
  return c.json(task)
})

app.delete("/tasks/:id", (c) => {
  const id = Number(c.req.param("id"))
  const ok = deleteTask(id)
  if (!ok) return c.json({ error: "Not found" }, 404)
  return c.json({ success: true })
})

const port = Number(process.env.PORT ?? 3000)
const host = process.env.HOST ?? "localhost"

serve({ fetch: app.fetch, port, hostname: host }, (info) => {
  console.log(`Server running at http://${host}:${info.port}`)
})
