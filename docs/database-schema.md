# Database Schema Documentation

## Overview
The WTUS Team System uses SQLite as its database system, as specified in the application configuration. This document describes the database schema, including tables, relationships, and key fields.

## Tables

### Users
Stores information about team members.

| Column     | Type    | Description                              |
|------------|---------|------------------------------------------|
| id         | INTEGER | Primary key                              |
| username   | TEXT    | User's login name (unique)               |
| email      | TEXT    | User's email address                     |
| password   | TEXT    | Hashed password                          |
| created_at | TEXT    | Timestamp when the user was created      |
| specialties| TEXT    | JSON-encoded list of user specialties    |

### Tasks
Stores information about tasks to be completed.

| Column      | Type    | Description                             |
|-------------|---------|-----------------------------------------|
| id          | INTEGER | Primary key                             |
| title       | TEXT    | Task title                              |
| description | TEXT    | Detailed description of the task        |
| status      | TEXT    | Current status (e.g., Pending, In Progress) |
| due_date    | TEXT    | Due date in ISO format                  |
| assigned_to | INTEGER | Foreign key to users.id                 |
| created_at  | TEXT    | Timestamp when the task was created     |
| updated_at  | TEXT    | Timestamp when the task was last updated|

### TaskComments
Stores comments on tasks.

| Column      | Type    | Description                             |
|-------------|---------|-----------------------------------------|
| id          | INTEGER | Primary key                             |
| task_id     | INTEGER | Foreign key to tasks.id                 |
| user_id     | INTEGER | Foreign key to users.id (commenter)     |
| content     | TEXT    | Comment content                         |
| created_at  | TEXT    | Timestamp when the comment was created  |

### Schedules
Stores user availability information.

| Column      | Type    | Description                             |
|-------------|---------|-----------------------------------------|
| id          | INTEGER | Primary key                             |
| user_id     | INTEGER | Foreign key to users.id                 |
| day_of_week | INTEGER | Day of week (0-6, where 0 is Monday)    |
| start_time  | TEXT    | Start time in HH:MM format             |
| end_time    | TEXT    | End time in HH:MM format               |

### Assets
Stores information about uploaded files.

| Column      | Type    | Description                             |
|-------------|---------|-----------------------------------------|
| id          | INTEGER | Primary key                             |
| filename    | TEXT    | Name of the file                        |
| filepath    | TEXT    | Path to the file on the server          |
| filetype    | TEXT    | MIME type of the file                   |
| filesize    | INTEGER | Size of the file in bytes               |
| uploaded_by | INTEGER | Foreign key to users.id                 |
| uploaded_at | TEXT    | Timestamp when the file was uploaded    |
| description | TEXT    | Optional description of the file        |

## Relationships

### User to Tasks
- One-to-many: A user can be assigned to multiple tasks
- Foreign key: tasks.assigned_to references users.id

### User to TaskComments
- One-to-many: A user can make multiple comments
- Foreign key: task_comments.user_id references users.id

### Task to TaskComments
- One-to-many: A task can have multiple comments
- Foreign key: task_comments.task_id references tasks.id

### User to Schedules
- One-to-many: A user can have multiple schedule entries
- Foreign key: schedules.user_id references users.id

### User to Assets
- One-to-many: A user can upload multiple files
- Foreign key: assets.uploaded_by references users.id

## Indexing Strategy
The following indexes are recommended to improve query performance:

1. users(username) - For quick user lookup during authentication
2. tasks(assigned_to) - For filtering tasks by assignee
3. tasks(status, due_date) - For filtering and sorting tasks
4. schedules(user_id, day_of_week) - For quickly retrieving a user's schedule
5. assets(uploaded_by) - For filtering files by uploader

## Data Integrity Constraints
- Cascading deletes are used for task comments when a task is deleted
- Foreign key constraints enforce referential integrity
- NOT NULL constraints on essential fields like username, email, task title

## Query Examples

### Get all tasks assigned to a specific user
```sql
SELECT * FROM tasks WHERE assigned_to = ?
```

### Get all comments for a specific task
```sql
SELECT tc.*, u.username 
FROM task_comments tc
JOIN users u ON tc.user_id = u.id
WHERE tc.task_id = ?
ORDER BY tc.created_at DESC
```

### Get user availability for a specific day
```sql
SELECT * FROM schedules 
WHERE user_id = ? AND day_of_week = ?
ORDER BY start_time
```

### Get files uploaded by a specific user
```sql
SELECT * FROM assets
WHERE uploaded_by = ?
ORDER BY uploaded_at DESC
```