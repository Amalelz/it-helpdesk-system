# Requirements: IT Helpdesk Ticketing System

## 1. Problem statement
A company with 200 employees receives IT issues by email, WhatsApp and phone calls.
Requests get lost, nobody knows who is handling what, and managers have no reports.
The company needs one system to raise, assign, track and resolve IT issues.

## 2. Users and roles
| Role | Permissions |
|---|---|
| Employee | Raise tickets, view and comment on own tickets |
| IT Agent | View tickets assigned to them, update status, comment |
| Admin | Everything an agent can do, plus manage users and roles, assign tickets, view dashboard |

## 3. Functional requirements (MVP)

**US-01 Register.** As an employee, I want to register so that my tickets are linked to me.
- Email must be unique and valid
- Password minimum 8 characters, stored hashed, never returned by any API
- New accounts get the Employee role by default

**US-02 Login.** As a user, I want to log in so that I can access the system.
- Valid credentials return a JWT access token with an expiry
- Invalid credentials return 401 without saying which field was wrong
- Protected endpoints return 401 without a valid token

**US-03 Raise a ticket.** As an employee, I want to raise a ticket so that IT knows what is broken.
- Title (max 150 chars) and description are required
- Priority is one of Low, Medium, High, Critical
- Ticket gets a unique ID like TKT-0001 and status Open
- Creator and creation time are recorded

**US-04 View my tickets.** As an employee, I want to see my tickets so that I can track progress.
- Returns only tickets created by me, newest first
- Response is paginated

**US-05 Ticket detail.** As a user, I want to open a ticket so that I can see its full history.
- Shows details, status, assignee, comments and history
- An employee opening another employee's ticket gets 403
- Unknown ID returns 404

**US-06 Comment.** As a ticket participant, I want to add comments so that we can communicate.
- Comment text is required and not blank
- Allowed for the ticket creator, the assigned agent and admins
- Each comment stores author and time

**US-07 Assign a ticket.** As an admin, I want to assign a ticket to an agent so that someone owns it.
- Only users with the Agent role can be assigned
- Non-admins get 403
- Assignment is recorded in the ticket history

**US-08 Update status.** As an agent, I want to update ticket status so that the requester knows progress.
- Statuses: Open, In Progress, Resolved, Closed
- Only valid transitions are allowed (Open to In Progress to Resolved to Closed)
- Invalid transitions return 400
- Only the assigned agent or an admin can change status

**US-09 Agent queue.** As an agent, I want to see tickets assigned to me so that I know my workload.
- Returns only my assigned tickets, sortable by priority and age

**US-10 Search and filter.** As a user, I want to search and filter tickets so that I can find them quickly.
- Filter by status, priority and assignee
- Keyword search on title and description
- Results respect role visibility (an employee never sees others' tickets)

**US-11 Manage users.** As an admin, I want to manage users and roles so that access is controlled.
- List users, change role, deactivate an account
- Deactivated users cannot log in
- Non-admins get 403

**US-12 Dashboard.** As an admin, I want summary counts so that I can see the workload.
- Counts by status and by priority
- Count of unassigned tickets and tickets older than 3 days that are still open

**US-13 Ticket history.** As an admin or agent, I want an audit trail so that changes are traceable.
- Every status change and assignment records who, what and when
- History cannot be edited or deleted through the API

**US-14 Reopen.** As an employee, I want to reopen a Resolved ticket so that unresolved issues are not lost.
- Allowed only for the ticket creator while status is Resolved
- Status returns to Open and the history records it

**US-15 Health check.** As an operator, I want a health endpoint so that monitoring can detect failures.
- `GET /health` returns 200 when the app and database are reachable
- Returns 503 when the database is not reachable

## 4. Non-functional requirements
| Area | Requirement |
|---|---|
| Security | Hashed passwords, JWT with expiry, role checks on the server, input validation, no secrets in Git |
| Performance | List endpoints paginated, common filter columns indexed |
| Reliability | Health check, daily database backup, tested restore |
| Observability | Structured application logs, request logging at the reverse proxy |
| Maintainability | Automated tests run in CI, linting, database migrations |
| Deployability | Runs from Docker Compose, deployed behind Nginx on Linux, HTTPS |

## 5. Phase 2 (after the MVP is working)
- File attachments and email notifications
- Network monitoring module (ping and port checks, uptime history, down alerts)
- Log analyzer module
- AI support bot over a knowledge base

## 6. Out of scope
Mobile app, billing, multi-company support, single sign-on.

## 7. Tech stack
FastAPI, SQLAlchemy, Alembic, MySQL, React, Docker, Docker Compose, GitHub Actions, Nginx, Ubuntu Server.