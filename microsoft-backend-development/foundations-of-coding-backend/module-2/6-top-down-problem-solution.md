# Step-by-Step Solution: Project Management Tool

## 1) Main goal (one sentence)

**Build a simple project management tool that lets teams create and track tasks, collaborate (comments/mentions), and see basic progress reports.**

---

## 2) Choose an approach (Top-Down vs Bottom-Up)

**Pick: Top-Down.**
Why? The high-level features are already clear (“task tracking”, “team collaboration”, “reporting”). With a clear target, it’s easier to start from the big picture (modules and APIs) and then refine into smaller pieces.

> Tip: We can still use tiny **bottom-up spikes** (small throwaway prototypes) for unknowns like “real-time updates” before we commit to them.

---

## 3) Define scope & non-functional needs (keep it small)

**MVP scope (must-haves):**

* Projects & tasks (title, description, status, assignee, due date).
* Collaboration via task comments and @mentions.
* Simple reports: task counts by status, tasks per assignee, and a basic burn-down or trend line.
* Auth (email/password) so data is private to a workspace/team.

**Nice-to-haves (later):** file attachments, notifications, Kanban board, real-time presence.

**Non-functionals (MVP targets):**

* Simple monolith backend, REST API, Postgres or SQLite, paging on list endpoints.
* Basic auth + role checks (Owner, Member).
* Tests for critical flows (create task, comment on task, report query).

---

## 4) High-level architecture (beginner-friendly)

* **Monolith**: one backend service (e.g., Node/Express, Django, or Spring Boot).
* **REST API** + JSON.
* **DB**: Postgres (or SQLite to start).
* **Frontend**: any (even a simple API client like Postman to begin).
* **Layers**: Routes/Controllers → Services → Repos/ORM → DB.

---

## 5) Data model (start simple)

Entities & key fields:

* **User**: id, name, email, password\_hash, role
* **Project**: id, name, description, owner\_id
* **Task**: id, project\_id, title, description, status (todo|doing|done), assignee\_id, due\_date, created\_at, updated\_at
* **Comment**: id, task\_id, author\_id, body, created\_at
* **(Optional) Mention**: id, comment\_id, mentioned\_user\_id

Relationships:

* Project has many Tasks.
* Task has many Comments.
* User can own projects, be assigned tasks, and author comments.

---

## 6) Feature breakdown → concrete tasks (Top-Down → smaller pieces)

### A) Authentication & Users

* **Stories**

  * As a user, I can sign up and sign in.
  * As a user, I can view/update my profile.
* **Backend tasks**

  * POST `/auth/signup`, `/auth/login` (return JWT/session).
  * GET `/me`, PATCH `/me`.
  * Password hashing, input validation, auth middleware.

### B) Projects

* **Stories**

  * As a user, I can create a project and invite teammates (optional later).
  * As a user, I can list my projects and view one project.
* **Backend tasks**

  * POST `/projects`, GET `/projects`, GET `/projects/:id`, PATCH `/projects/:id`.
  * Ownership/role checks.

### C) Task Tracking

* **Stories**

  * As a user, I can create tasks in a project and update status (todo/doing/done).
  * As a user, I can assign tasks to a teammate and set due dates.
* **Backend tasks**

  * POST `/projects/:id/tasks`, GET `/projects/:id/tasks?status=…&assignee=…&page=…`
  * GET `/tasks/:taskId`, PATCH `/tasks/:taskId`, DELETE `/tasks/:taskId`
  * Validation, pagination, sorting, authorization.

### D) Team Collaboration (Comments & Mentions)

* **Stories**

  * As a user, I can comment on a task and @mention a teammate.
  * As a user, I can see the conversation thread for a task.
* **Backend tasks**

  * POST `/tasks/:taskId/comments`, GET `/tasks/:taskId/comments`
  * Detect `@username` in comment body → store mentions (optional MVP)
  * (Later) notifications/webhooks

### E) Reporting

* **Stories**

  * As a user, I can see counts by status for a project (e.g., how many todo/doing/done).
  * As a user, I can see tasks per assignee and a simple trend over time.
* **Backend tasks**

  * GET `/reports/status?projectId=…`
  * GET `/reports/assignees?projectId=…`
  * GET `/reports/trends?projectId=…&range=last_14_days`
  * Efficient SQL aggregations or ORM queries; add indexes on `project_id`, `assignee_id`, `status`.

---

## 7) Example API sketch (keep it tangible)

```
POST   /auth/signup
POST   /auth/login
GET    /me
PATCH  /me

POST   /projects
GET    /projects
GET    /projects/:id
PATCH  /projects/:id

POST   /projects/:id/tasks
GET    /projects/:id/tasks
GET    /tasks/:taskId
PATCH  /tasks/:taskId
DELETE /tasks/:taskId

POST   /tasks/:taskId/comments
GET    /tasks/:taskId/comments

GET    /reports/status          (projectId)
GET    /reports/assignees       (projectId)
GET    /reports/trends          (projectId, range)
```

---

## 8) Implementation order (small, safe steps)

1. **Project skeleton + DB** (health check route, migrations, ORM).
2. **Auth & Users** (signup/login, JWT/session, `/me`).
3. **Projects** (CRUD read-heavy; role checks).
4. **Tasks** (CRUD, filters, indexes; this unlocks most value).
5. **Comments** (threaded collaboration).
6. **Reports** (simple aggregations first).
7. **Polish** (validation errors, pagination defaults, basic rate limiting).

> After each step: write a few tests and try endpoints in Postman/Insomnia.

---

## 9) Why Top-Down fits (clear and simple)

* The **high-level requirements are clear**, so we can confidently design modules and their interfaces first.
* Top-Down decomposition helps beginners avoid “rabbit holes,” keeping focus on **MVP**.
* We still keep flexibility by doing tiny **bottom-up spikes** for tricky parts (e.g., try a quick aggregation query before building the reporting APIs).

---

## 10) Common pitfalls to watch for (and easy fixes)

**Pitfall:** Over-designing reports too early.
**Fix:** Start with two simple aggregates (by status, by assignee). Add trends later.

**Pitfall:** Unclear authorization rules.
**Fix:** Write 3–5 examples (“Only project members can …”) and test them explicitly.

**Pitfall:** Task lists that time out with no indexes.
**Fix:** Add DB indexes on `(project_id)`, `(project_id, status)`, `(assignee_id)` early.

**Pitfall:** Bloated responses.
**Fix:** Support pagination (`?page=1&pageSize=20`) and minimal fields (select lists vs details).

---

## 11) Minimal tech stack (beginner-friendly)

* **Language/Framework (pick one):**

  * Node.js + Express + Prisma (Postgres)
  * Python + Django REST Framework (SQLite/Postgres)
  * Java + Spring Boot + JPA (Postgres)
* **Auth:** JWT (http-only cookie or Authorization header)
* **DB:** Postgres (start with SQLite if using Django to keep friction low)
* **Dev utilities:** Postman/Insomnia, Docker (optional), Jest/pytest/JUnit, ESLint/Black/Checkstyle

---

## 12) Simple acceptance checklist (you can test these today)

* [ ] I can **sign up, log in**, and call `/me` to see my profile.
* [ ] I can **create a project**, list my projects, and fetch one project.
* [ ] I can **create a task** under a project, **assign** it, **change status**, and **list** tasks with filters.
* [ ] I can **comment** on a task and read the comment thread.
* [ ] I can load **/reports/status** and **/reports/assignees** and the numbers look correct.

---

### TL;DR

* **Approach:** Top-Down (with tiny bottom-up spikes for unknowns).
* **Breakdown:** Auth → Projects → Tasks → Comments → Reports.
* **Deliver incrementally**, test each slice, and keep scope small for the MVP.