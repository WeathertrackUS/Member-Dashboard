# Code Structure and Organization

## Overview
This document outlines the structure and organization of the WTUS Team System codebase, providing an overview of the directories, files, and their purposes. Understanding this structure will help new developers navigate the project more effectively.

## Project Structure
The WTUS Team System is organized into two main parts: the backend (Flask) and the frontend (React). Here's a high-level overview of the project structure:

```
wtus-team-system/
├── backend/             # Backend Flask application
├── frontend/            # Frontend React application
├── docs/                # Project documentation
├── tests/               # Test suite
├── README.md            # Project overview
└── .gitignore           # Git ignore file
```

## Backend Structure

```
backend/
├── app/                 # Main application package
│   ├── __init__.py      # Application initialization
│   ├── auth/            # Authentication related modules
│   │   └── routes.py    # Auth endpoints
│   ├── models/          # Data models
│   │   ├── schedule.py  # Schedule model
│   │   ├── task.py      # Task model
│   │   └── user.py      # User model
│   ├── routes/          # API endpoints
│   │   ├── assets.py    # File management endpoints
│   │   ├── schedule.py  # Schedule management endpoints
│   │   └── tasks.py     # Task management endpoints
│   └── utils/           # Utility functions
│       └── helpers.py   # Helper functions
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── run.py               # Application entry point
└── uploads/             # Directory for uploaded files
```

### Key Files and Their Purpose

#### Application Initialization
- **backend/app/__init__.py**: Initializes the Flask application and registers blueprints for different parts of the API.

#### Configuration
- **backend/config.py**: Contains configuration settings for the application, including database connection, secret key, and file upload settings.

#### Application Entry Point
- **backend/run.py**: The main entry point for running the Flask application. It creates the app instance and starts the server.

#### Authentication
- **backend/app/auth/routes.py**: Contains the routes for user authentication, including registration and login.

#### Models
- **backend/app/models/user.py**: Defines the User model representing team members.
- **backend/app/models/task.py**: Defines the Task model for task management.
- **backend/app/models/schedule.py**: Defines the Schedule model for user availability.

#### Routes
- **backend/app/routes/tasks.py**: API endpoints for task management.
- **backend/app/routes/schedule.py**: API endpoints for schedule management.
- **backend/app/routes/assets.py**: API endpoints for file management.

#### Utilities
- **backend/app/utils/helpers.py**: Contains utility functions used throughout the application.

## Frontend Structure

```
frontend/
├── index.html          # Main HTML file
├── package.json        # Node.js dependencies and scripts
└── src/                # Source code
    ├── App.js          # Main React component
    ├── components/     # React components
    │   ├── Calendar.js      # Calendar component
    │   ├── Dashboard.js     # Dashboard component
    │   ├── FileManager.js   # File manager component
    │   └── TaskBoard.js     # Task board component
    └── styles/         # CSS styles
        └── main.css    # Main stylesheet
```

### Key Files and Their Purpose

#### HTML and Configuration
- **frontend/index.html**: The main HTML file that serves as the entry point for the React application.
- **frontend/package.json**: Defines the project's dependencies, scripts, and metadata.

#### React Components
- **frontend/src/App.js**: The main React component that sets up routing and the overall application structure.
- **frontend/src/components/Dashboard.js**: The dashboard component showing an overview of tasks and schedules.
- **frontend/src/components/TaskBoard.js**: The task management interface.
- **frontend/src/components/FileManager.js**: The file management interface.
- **frontend/src/components/Calendar.js**: The calendar component for managing user availability.

#### Styles
- **frontend/src/styles/main.css**: Contains CSS styles for the application.

## Documentation Structure

```
docs/
├── 01-project-overview.md          # Project overview and purpose
├── 02-backend-architecture.md      # Backend architecture details
├── 03-frontend-architecture.md     # Frontend architecture details
├── 04-database-schema.md           # Database schema documentation
├── 05-api-documentation.md         # API endpoint documentation
├── 06-deployment-guide.md          # Deployment instructions
├── 07-contribution-guide.md        # Guide for contributors
└── 08-code-structure.md            # This document
```

## Tests Structure

```
tests/
└── __init__.py                  # Package initialization
```

The tests directory will be expanded as more tests are added to the project.

## Code Organization Principles

### Backend Principles
1. **Separation of Concerns**: Each module has a specific purpose.
2. **Blueprints**: Flask blueprints are used to organize related routes.
3. **Model-View-Controller (MVC)**: The backend follows an MVC-like pattern:
   - Models (app/models/): Define data structures
   - Views (app/routes/): Handle API requests and responses
   - Controllers: Logic is embedded in route handlers or separate utility functions

### Frontend Principles
1. **Component-Based Architecture**: UI is built from reusable React components.
2. **Container/Presentational Pattern**: Some components focus on logic, others on presentation.
3. **Single Responsibility**: Each component should have one main responsibility.

## Naming Conventions

### Backend
- Files: snake_case (e.g., user_profile.py)
- Classes: PascalCase (e.g., UserProfile)
- Functions and variables: snake_case (e.g., get_user_profile)
- Constants: UPPER_SNAKE_CASE (e.g., MAX_UPLOAD_SIZE)

### Frontend
- Files: PascalCase for components (e.g., TaskBoard.js)
- Variables and functions: camelCase (e.g., getUserData)
- Constants: UPPER_SNAKE_CASE (e.g., API_ENDPOINT)

## Code Flow

### Backend Request Flow
1. Request arrives at a route defined in one of the blueprint files
2. Route handler processes the request
3. If needed, the handler interacts with models to fetch or modify data
4. The handler returns a response, typically in JSON format

### Frontend Data Flow
1. Component mounts and may fetch data in useEffect
2. User interactions trigger event handlers
3. Event handlers may update local state or make API calls
4. State changes cause component re-renders
5. Changes may propagate to child components through props

## Future Organization Considerations
As the project grows, consider:
1. Implementing a state management solution (Redux, Context API)
2. Breaking down large components into smaller ones
3. Adding more structure to the utils directory
4. Organizing CSS with a methodology like BEM or using CSS modules/styled-components