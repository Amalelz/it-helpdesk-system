# REST API Design

Base path: `/api/v1`. JSON everywhere. Auth: `Authorization: Bearer <JWT>`.
Errors use FastAPI's format: `{"detail": "message"}`.

## Endpoints

| Method | Path | Who | Purpose | Success | Errors |
|---|---|---|---|---|---|
| POST | /auth/register | public | Create employee account | 201 | 400, 409 email exists, 422 |
| POST | /auth/login | public | Get JWT | 200 | 401 |
| GET | /auth/me | any | Current user | 200 | 401 |
| GET | /categories | any | List categories | 200 | 401 |
| POST | /tickets | any | Create ticket | 201 | 401, 422 |
| GET | /tickets | any | List tickets (scoped by role) | 200 | 401 |
| GET | /tickets/{id} | owner, assignee, admin | Ticket detail | 200 | 401, 403, 404 |
| PATCH | /tickets/{id}/status | assignee, admin | Change status | 200 | 400 invalid transition, 403, 404 |
| PATCH | /tickets/{id}/assign | admin | Assign to an agent | 200 | 400 not an agent, 403, 404 |
| POST | /tickets/{id}/reopen | creator | Reopen a Resolved ticket | 200 | 400, 403, 404 |
| GET | /tickets/{id}/comments | participants, admin | List comments | 200 | 403, 404 |
| POST | /tickets/{id}/comments | participants, admin | Add comment | 201 | 403, 404, 422 |
| GET | /tickets/{id}/history | agent, admin | Audit trail | 200 | 403, 404 |
| GET | /users | admin | List users (`?role=agent`) | 200 | 403 |
| PATCH | /users/{id}/role | admin | Change role | 200 | 403, 404 |
| PATCH | /users/{id}/active | admin | Activate or deactivate | 200 | 403, 404 |
| GET | /dashboard/stats | admin | Counts for dashboard | 200 | 403 |
| GET | /health | public | App and database health | 200 | 503 |

## List behaviour
`GET /tickets` is scoped by role: employees see tickets they created, agents see
tickets assigned to them, admins see all. Query params: `status`, `priority`,
`assignee_id`, `q` (keyword in title or description), `sort` (`created_at`,
`priority`), `order`, `page` (default 1), `limit` (default 20, max 100).

Response:
```json
{ "items": [ ... ], "total": 57, "page": 1, "limit": 20 }
```

## Example: create ticket
`POST /api/v1/tickets`
```json
{ "title": "VPN not connecting", "description": "Timeout since morning",
  "priority": "high", "category_id": 3 }
```
`201 Created`
```json
{ "id": 1, "ticket_no": "TKT-0001", "title": "VPN not connecting",
  "status": "open", "priority": "high", "created_by": 12, "assigned_to": null,
  "created_at": "2026-11-20T09:15:00Z" }
```

## Dashboard response
```json
{ "by_status": {"open": 8, "in_progress": 5, "resolved": 3, "closed": 41},
  "by_priority": {"low": 10, "medium": 30, "high": 12, "critical": 5},
  "unassigned": 4, "open_older_than_3_days": 2 }
```

## Rules
- Role checks happen on the server for every endpoint, never only in the UI.
- Passwords and hashes are never returned.
- Login failures return the same 401 message for wrong email and wrong password.
- Health: 200 if the database answers a `SELECT 1`, otherwise 503.