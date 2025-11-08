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

## Documentation

Comprehensive documentation is available in the `docs` directory:

- [Project Overview](docs/project-overview.md)
- [Backend Architecture](docs/backend-architecture.md)
- [Frontend Architecture](docs/frontend-architecture.md)
- [Database Schema](docs/database-schema.md)
- [API Documentation](docs/api-documentation.md)
- [Deployment Guide](docs/deployment-guide.md)
- [Contribution Guide](docs/contribution-guide.md)
- [Code Structure](docs/code-structure.md)
- [Troubleshooting Guide](docs/troubleshooting-guide.md)
- [Security Best Practices](docs/security-best-practices.md)

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
├── docs
│   ├── project-overview.md
│   ├── backend-architecture.md
│   └── ... (other documentation files)
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
├── Security.md
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 14+ and npm

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

## Security

Please see our [Security Policy](Security.md) for information about reporting vulnerabilities and our security practices.

## Contributing

We welcome contributions to the WTUS Team System! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
