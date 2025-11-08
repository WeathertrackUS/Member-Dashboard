# Frontend Architecture

## Overview
The frontend of the WTUS Team System is built with React, providing an interactive and responsive user interface. It consumes the RESTful API endpoints provided by the backend to display and manage data related to tasks, schedules, and assets.

## Project Structure
```
frontend/
├── index.html             # Main HTML file
├── package.json           # Node.js dependencies and scripts
└── src/
    ├── App.js             # Main application component
    ├── components/        # React components
    │   ├── Calendar.js    # User availability calendar
    │   ├── Dashboard.js   # Main dashboard view
    │   ├── FileManager.js # File management interface
    │   └── TaskBoard.js   # Task management interface
    └── styles/
        └── main.css       # CSS styles
```

## Key Components

### App.js
The main application component that sets up routing using React Router. It defines the following routes:
- `/calendar` - Renders the Calendar component
- `/dashboard` - Renders the Dashboard component (also the default route)
- `/file-manager` - Renders the FileManager component
- `/task-board` - Renders the TaskBoard component

### Dashboard.js
The main dashboard view that provides an overview of team schedules and tasks. Currently a placeholder with basic structure for future development.

### TaskBoard.js
Implements the task management functionality, including:
- Displaying a list of tasks
- Adding new tasks with title, status, and due date
- Viewing task details including comments

### FileManager.js
Provides file management functionality, including:
- Displaying a list of available files
- Downloading files

### Calendar.js
A placeholder component for the user availability calendar, which will allow users to input and view schedule information.

## State Management
The application currently uses React's built-in state management with `useState` and `useEffect` hooks for component-level state. API calls are made directly from the components.

Example from TaskBoard.js:
```jsx
const [tasks, setTasks] = useState([]);
const [newTask, setNewTask] = useState({ title: '', status: '', dueDate: '', comments: [] });

useEffect(() => {
    // Fetch tasks from the backend
    const fetchTasks = async () => {
        const response = await fetch('/api/tasks');
        const data = await response.json();
        setTasks(data);
    };
    fetchTasks();
}, []);
```

## API Integration
Components make requests to the backend API using the built-in `fetch` API. For example:

```javascript
// Fetching data
const fetchFiles = async () => {
    try {
        const response = await fetch('/api/assets');
        const data = await response.json();
        setFiles(data);
    } catch (error) {
        console.error('Error fetching files:', error);
    }
};

// Posting data
const handleAddTask = async () => {
    const response = await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTask),
    });
    const addedTask = await response.json();
    setTasks([...tasks, addedTask]);
    setNewTask({ title: '', status: '', dueDate: '', comments: [] });
};
```

## Styling
The application uses CSS for styling, with styles defined in `src/styles/main.css`. The current CSS file is minimal and will be expanded as the UI is developed further.

## Dependencies
Key dependencies include:
- React 17.0.2
- React DOM 17.0.2
- React Scripts 4.0.3

Development dependencies:
- ESLint 7.32.0
- ESLint Plugin React 7.27.1

## Future Enhancements
Planned enhancements for the frontend include:
1. Implementation of a global state management solution (e.g., Redux or Context API)
2. Integration of a UI component library for consistent styling
3. Form validation for user inputs
4. Enhanced error handling and user feedback
5. Full implementation of the Calendar component
6. Responsive design for mobile compatibility