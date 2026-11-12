# Requirements: IT Helpdesk Ticketing System

## 1. Problem statement
A company with 200 employees receives IT issues by email, WhatsApp and phone calls.
Requests get lost, nobody knows who is handling what, and managers have no reports.
The company needs one system to raise, assign, track and resolve IT issues.

## 2. Users
| Role | Can do |
|---|---|
| Employee | Raise tickets, view own tickets, comment |
| IT Agent | View assigned tickets, update status, comment |
| Admin | Manage users, assign tickets, view dashboard |

## 3. User stories
### MVP (must have)
**US-01** As an employee, I want to register and log in, so that my tickets are linked to me.
- Acceptance criteria:
  - Email must be unique
  - Password is stored hashed, never in plain text
  - Wrong credentials return an error without saying which field was wrong

**US-02** As an employee, I want to raise a ticket with title, description and priority, so that IT knows what is broken.
- Acceptance criteria:
  - Title and description are required
  - Priority is Low, Medium, High or Critical
  - Ticket gets a unique ID like TKT-0001
  - Status starts as Open

**US-03** ... (you write the rest)

### Later (nice to have)
- Email notifications, file attachments, AI support bot

## 4. Out of scope
- Mobile app, payments, multi-company support