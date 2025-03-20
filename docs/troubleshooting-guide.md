# Troubleshooting Guide

## Overview
This guide provides solutions to common issues you might encounter when developing, deploying, or using the WTUS Team System. Use this document as a reference when you run into problems.

## Backend Issues

### Application Won't Start

#### Issue: ModuleNotFoundError
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
1. Ensure your virtual environment is activated
2. Install the required dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

#### Issue: Address Already in Use
```
OSError: [Errno 98] Address already in use
```

**Solution:**
1. Find the process using the port:
   ```bash
   # On Linux/macOS
   lsof -i :5000
   
   # On Windows
   netstat -ano | findstr :5000
   ```
2. Kill the process:
   ```bash
   # On Linux/macOS
   kill -9 <PID>
   
   # On Windows
   taskkill /F /PID <PID>
   ```

#### Issue: ImportError in Flask Application
```
ImportError: cannot import name 'something' from 'somewhere'
```

**Solution:**
1. Check that all required modules are installed
2. Verify the import paths in your Python files
3. Make sure your project structure matches the expected imports

### Database Issues

#### Issue: SQLite Database Locked
```
sqlite3.OperationalError: database is locked
```

**Solution:**
1. Ensure no other process is accessing the database file
2. Restart your Flask application
3. If the issue persists, try closing all connections and recreating the database file

#### Issue: Table Doesn't Exist
```
sqlite3.OperationalError: no such table: users
```

**Solution:**
1. Check if your database migrations have been run
2. Verify table names in your SQL queries
3. If needed, initialize the database manually:
   ```python
   # Create a script that sets up your database schema
   from app import db
   db.create_all()
   ```

#### Issue: Cannot Connect to PostgreSQL (Production)
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server
```

**Solution:**
1. Verify database credentials in your environment variables
2. Check if the PostgreSQL server is running
3. Ensure the database exists and the user has proper permissions
4. Check network connectivity between your application and the database server

### API Issues

#### Issue: 404 Not Found for API Endpoints
**Solution:**
1. Check the URL path you're using
2. Verify that the route is correctly defined in the blueprint
3. Ensure the blueprint is registered in the Flask application
4. Check for typos in the route definition

#### Issue: 500 Internal Server Error
**Solution:**
1. Check the application logs for detailed error information
2. Verify that request data matches the expected format
3. Check for uncaught exceptions in your route handlers
4. Ensure your database connection is working

#### Issue: CORS Errors
```
Access to fetch at 'http://localhost:5000/api/tasks' from origin 'http://localhost:3000' has been blocked by CORS policy
```

**Solution:**
1. Ensure Flask-CORS is properly installed and configured
2. Add the following configuration to your Flask app:
   ```python
   from flask_cors import CORS
   
   app = Flask(__name__)
   CORS(app)
   ```
3. For more specific CORS rules, configure the resources parameter:
   ```python
   CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
   ```

## Frontend Issues

### Build or Start Issues

#### Issue: Node Modules Not Found
```
Error: Cannot find module 'react'
```

**Solution:**
1. Install node modules:
   ```bash
   npm install
   ```
2. If the issue persists, delete the node_modules directory and reinstall:
   ```bash
   rm -rf node_modules
   npm install
   ```

#### Issue: JavaScript Heap Out of Memory
```
FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory
```

**Solution:**
1. Increase the memory allocated to Node.js:
   ```bash
   # For npm start
   NODE_OPTIONS=--max_old_space_size=4096 npm start
   
   # For npm build
   NODE_OPTIONS=--max_old_space_size=4096 npm run build
   ```

#### Issue: Port Already in Use
```
Something is already running on port 3000.
```

**Solution:**
1. Choose a different port:
   ```bash
   # For Create React App
   PORT=3001 npm start
   ```
2. Or find and kill the process using port 3000 (see backend section for commands)

### React Component Issues

#### Issue: Component Not Rendering
**Solution:**
1. Check for JavaScript errors in the browser console
2. Verify that the component is being imported and used correctly
3. Check if conditional rendering logic is preventing the component from displaying
4. Ensure that necessary props are being passed to the component

#### Issue: API Data Not Loading
**Solution:**
1. Check the browser console for network errors
2. Verify that your API request is correctly formatted
3. Ensure the API endpoint is correct and accessible
4. Check if your useEffect dependency array is configured properly:
   ```jsx
   useEffect(() => {
     fetchData();
   }, []); // Empty array means run once on component mount
   ```

#### Issue: React Router Not Working
**Solution:**
1. Ensure you're using the correct version of react-router-dom
2. Check your route definitions in App.js
3. Verify that you've wrapped your application with a Router component
4. For nested routes, ensure the parent route has a trailing /* or uses an Outlet component

### Styling Issues

#### Issue: CSS Not Applying
**Solution:**
1. Check if the CSS file is imported in your component or index.js
2. Verify class names for typos
3. Check browser developer tools to see if CSS rules are being overridden
4. Ensure that the CSS file is being included in the build process

## Deployment Issues

### Server Configuration

#### Issue: 502 Bad Gateway with Nginx
**Solution:**
1. Check if your backend application is running
2. Verify Nginx proxy settings:
   ```nginx
   location / {
       proxy_pass http://127.0.0.1:8000;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
   }
   ```
3. Check Nginx error logs:
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```

#### Issue: Application Crashes in Production
**Solution:**
1. Check application logs:
   ```bash
   sudo journalctl -u wtus-backend
   ```
2. Ensure environment variables are set correctly
3. Verify that database connections are properly closed
4. Add error handling to prevent crashes

### Docker Issues

#### Issue: Container Exits Immediately
**Solution:**
1. Check container logs:
   ```bash
   docker logs <container_id>
   ```
2. Ensure your CMD or ENTRYPOINT is correct
3. Check for environment variables that might be missing
4. Verify file permissions inside the container

#### Issue: Cannot Connect to Database from Docker
**Solution:**
1. For a separate database container, ensure they're on the same Docker network
2. If using localhost in connection string, change to the actual host IP or service name
3. Verify that database port is exposed and mapped correctly
4. Check that database credentials are correct

## File Management Issues

### Issue: File Upload Fails
**Solution:**
1. Check that the uploads directory exists and has correct permissions
2. Verify that the file size doesn't exceed limits
3. Check that the file type is allowed in your configuration
4. Ensure your form has the correct enctype: `enctype="multipart/form-data"`

### Issue: Cannot Download Files
**Solution:**
1. Verify that the file exists in the expected location
2. Check file permissions
3. Ensure the download route is properly configured
4. Verify that `send_from_directory` is used correctly:
   ```python
   @app.route('/download/<filename>')
   def download(filename):
       return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
   ```

## Authentication Issues

### Issue: Login Not Working
**Solution:**
1. Verify username and password are correct
2. Check if the user exists in the database
3. Ensure passwords are being hashed and compared correctly
4. Check for CSRF token issues if applicable

### Issue: Session Not Persisting
**Solution:**
1. Verify that your secret key is set and not changing between restarts
2. Check that cookies are being stored (browser developer tools)
3. Ensure that the session configuration is correct

## Performance Issues

### Slow API Responses
**Solution:**
1. Add indexes to frequently queried database columns
2. Optimize database queries
3. Implement caching for expensive operations
4. Consider pagination for large data sets

### Frontend Performance Issues
**Solution:**
1. Use React's production build for deployment
2. Implement code splitting for large applications
3. Optimize images and other assets
4. Use memoization for expensive calculations

## Contacting Support
If you've tried the solutions above and are still experiencing issues:

1. Check existing issues in the GitHub repository
2. Create a new issue with detailed information:
   - Description of the problem
   - Steps to reproduce
   - Expected vs. actual behavior
   - Relevant logs or error messages
   - Environment information (OS, browser, versions)

## Preventative Measures
To avoid common issues:

1. Regularly update dependencies
2. Add comprehensive error handling
3. Implement logging throughout the application
4. Write automated tests for critical functionality
5. Create a staging environment for testing before production deployment