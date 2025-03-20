# Backend Architecture

## Overview
The backend of the WTUS Team System is built with Flask, a lightweight Python web framework. It provides RESTful API endpoints that the frontend consumes to manage data related to users, tasks, schedules, and assets.

## Project Structure
```
backend/
├── app/                  # Main application package
│   ├── __init__.py       # Application initialization
│   ├── auth/             # Authentication related modules
│   │   └── routes.py     # Auth endpoints (login, register)
│   ├── models/           # Data models
│   │   ├── schedule.py   # Schedule model
│   │   ├── task.py       # Task model
│   │   └── user.py       # User model
│   ├── routes/           # API endpoints
│   │   ├── assets.py     # File management endpoints
│   │   ├── schedule.py   # Schedule management endpoints
│   │   └── tasks.py      # Task management endpoints
│   └── utils/            # Utility functions
│       └── helpers.py    # Helper functions
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
└── run.py                # Application entry point
```

## API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /login` - Authenticate a user

### Tasks
- `GET /tasks` - Retrieve all tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/<task_id>` - Update a specific task
- `DELETE /tasks/<task_id>` - Delete a specific task

### Schedules
- `GET /schedules` - Retrieve all schedules
- `GET /schedules/<user_id>` - Retrieve schedule for a specific user
- `POST /schedules` - Create a new schedule
- `PUT /schedules/<schedule_id>` - Update a specific schedule
- `DELETE /schedules/<schedule_id>` - Delete a specific schedule

### Assets
- `GET /assets` - List all available files
- `GET /assets/<filename>` - Download a specific file

## Data Models

### User Model
The User model represents team members and stores their authentication details and specialties.

Key attributes:
- `user_id`: Unique identifier for the user
- `username`: User's login name
- `email`: User's email address
- `specialties`: List of user's areas of expertise

### Task Model
The Task model represents work items that need to be completed.

Key attributes:
- `title`: Task title
- `description`: Detailed task description
- `status`: Current task status (e.g., Pending, In Progress, Completed)
- `due_date`: Date by which the task should be completed
- `assigned_to`: User assigned to the task

### Schedule Model
The Schedule model tracks user availability.

Key attributes:
- `user_id`: ID of the user whose schedule this is
- `availability`: List of time slots when the user is available

## Configuration
The application's configuration is managed in `config.py`, which includes settings for:
- Secret key
- Database URI
- Debug mode
- Allowed file extensions
- Upload folder path

## Database
Currently, the application is configured to use SQLite, with the database file stored at the location specified in the configuration. The database schema reflects the data models described above.

## File Storage
The system stores uploaded files in the `uploads` directory. The allowed file extensions are configured in `config.py` and currently include common image formats and PSD files (.psd, .jpg, .jpeg, .png, .gif).

## Dependencies
Key dependencies include:
- Flask 2.2.5
- Flask-Cors 4.0.2
- Flask-SQLAlchemy 2.5.1
- Flask-Migrate 3.1.0
- python-dotenv 0.17.1
- requests 2.32.2