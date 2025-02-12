# wtus-team-system/wtus-team-system/README.md

# WTUS Team System

Welcome to the WTUS Team System project! This application is designed to facilitate team collaboration by providing features for scheduling, task management, and file sharing.

## Features

- **User Availability**: Members can input their availability in a graphical format.
- **Schedule Display**: View individual and team schedules based on specialties.
- **File Management**: Host and manage downloadable files (e.g., .psd files) for team use.
- **Task Dashboard**: Create and manage tasks with features such as:
  - Assigning team members
  - Task status updates
  - Labels for categorization (e.g., Twitter, Severe Weather)
  - Due dates
  - Comment/discussion board for each task

## Project Structure

```
wtus-team-system
├── backend
│   ├── app
│   ├── config.py
│   ├── requirements.txt
│   └── run.py
├── frontend
│   ├── src
│   ├── package.json
│   └── index.html
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the backend directory and install dependencies:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Navigate to the frontend directory and install dependencies:
   ```
   cd frontend
   npm install
   ```

### Running the Application

- To run the backend:
  ```
  python run.py
  ```

- To run the frontend, navigate to the frontend directory and use:
  ```
  npm start
  ```

## Hosting Options

For hosting the application, consider the following options:

- **Heroku**: Offers a free tier for hosting applications.
- **Vercel**: Great for frontend applications with easy deployment.
- **GitHub Pages**: Suitable for static frontend hosting.
- **DigitalOcean**: Affordable VPS options for backend hosting.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.