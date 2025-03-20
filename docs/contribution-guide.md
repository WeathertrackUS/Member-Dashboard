# Contribution Guide

## Welcome to the WTUS Team System Project

Thank you for your interest in contributing to the WTUS Team System! This guide will help you understand the contribution process and the project standards.

## Getting Started

### Prerequisites
Before you begin contributing, make sure you have:
- A GitHub account
- Git installed on your local machine
- Python 3.9+ installed
- Node.js and npm installed
- Basic knowledge of Python, Flask, React, and JavaScript

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub.

2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/your-username/wtus-team-system.git
   cd wtus-team-system
   ```

3. **Add the original repository as an upstream remote**:
   ```bash
   git remote add upstream https://github.com/original-owner/wtus-team-system.git
   ```

4. **Set up the development environment**:
   - Follow the instructions in the [Deployment Guide](06-deployment-guide.md) to set up your local development environment.

## Contribution Workflow

### 1. Choose or Create an Issue
- Look for open issues in the GitHub repository
- If you found a bug or have a feature idea, create a new issue
- Comment on the issue you'd like to work on to let others know

### 2. Create a Branch
Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-name
```

Use a descriptive branch name that reflects the changes you're making.

### 3. Make Your Changes
- Follow the code style and guidelines described below
- Write tests for your changes when applicable
- Keep your changes focused and related to the issue you're addressing

### 4. Test Your Changes
- Run the existing test suite to ensure you haven't broken anything:
  ```bash
  # For backend tests
  cd backend
  python -m unittest discover tests

  # For frontend tests
  cd frontend
  npm test
  ```
- Manually test your changes to ensure they work as expected

### 5. Commit Your Changes
- Write clear and descriptive commit messages
- Reference the issue number in your commit message:
  ```
  feat: Add user availability calendar functionality (#42)
  ```
- Use conventional commit format:
  - `feat:` for features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `test:` for adding or modifying tests
  - `refactor:` for code refactoring
  - `style:` for formatting changes
  - `chore:` for build process or tooling changes

### 6. Keep Your Branch Updated
Regularly sync your branch with the upstream repository:
```bash
git fetch upstream
git rebase upstream/main
```

### 7. Push Your Changes
Push your changes to your fork:
```bash
git push origin your-branch-name
```

### 8. Submit a Pull Request
- Go to the GitHub repository page and create a new pull request
- Provide a clear description of your changes
- Reference the issue your pull request addresses
- Wait for maintainers to review your code

### 9. Address Review Feedback
- Be responsive to review comments
- Make requested changes and push them to your branch
- Discuss any disagreements respectfully

## Code Style Guidelines

### Python (Backend)
- Follow PEP 8 style guidelines
- Use 4 spaces for indentation
- Maximum line length of 151 characters (as per DeepSource configuration)
- Use docstrings for functions, classes, and modules
- Use type hints when appropriate

Example:
```python
def get_user_schedule(user_id: int) -> dict:
    """
    Retrieve the schedule for a specific user.

    Args:
        user_id: The ID of the user

    Returns:
        A dictionary containing the user's schedule information
    """
    # Function implementation
```

### JavaScript/React (Frontend)
- Use ESLint with the project's configuration
- Use 2 spaces for indentation
- Use camelCase for variables and functions
- Use PascalCase for component names
- Add comments for complex logic
- Prefer functional components over class components

Example:
```javascript
/**
 * Component for displaying a user's tasks
 * @param {Object} props - Component props
 * @param {Array} props.tasks - List of tasks to display
 */
const TaskList = ({ tasks }) => {
  const renderTaskItem = (task) => {
    return (
      <li key={task.id}>
        <h3>{task.title}</h3>
        <p>Status: {task.status}</p>
      </li>
    );
  };

  return (
    <div className="task-list">
      <h2>Your Tasks</h2>
      <ul>
        {tasks.map(renderTaskItem)}
      </ul>
    </div>
  );
};
```

## Documentation Standards

### Code Documentation
- Document all public functions, classes, and modules
- Use clear parameter descriptions
- Explain return values
- Document exceptions that might be raised

### Project Documentation
- Update relevant documentation when making changes
- If you add a new feature, add documentation for it
- If you change existing behavior, update documentation to reflect the changes

## Testing Guidelines

### Backend Tests
- Write unit tests for new functionality
- Place tests in the `tests` directory
- Follow the existing test structure
- Name test files with a `_test.py` suffix

### Frontend Tests
- Write unit tests for React components
- Test component rendering and behavior
- Mock API calls when testing components that fetch data

## Pull Request Guidelines

A good pull request should:
- Address a single concern (feature or bug fix)
- Include tests for the new code
- Update documentation as needed
- Pass all CI checks
- Have a clear, descriptive title
- Include a detailed description of changes
- Use a verified signiture

## Community Guidelines

When participating in this project, please:
- Be respectful and inclusive in your communications
- Provide constructive feedback
- Help others who are contributing to the project
- Follow the code of conduct

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with your question
- Contact the project maintainers
- Ask for clarification on an existing issue or pull request

Thank you for contributing to the WTUS Team System project!