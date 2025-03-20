# Deployment Guide

## Overview
This guide provides instructions for deploying the WTUS Team System in both development and production environments. It covers setting up the backend, frontend, and database configurations.

## Prerequisites
Before deploying the application, ensure you have the following installed:

- Python 3.9+ (tested with 3.9, 3.10, 3.11, 3.12, 3.13)
- Node.js 14+ and npm
- Git (for version control)
- A code editor (e.g., VS Code, PyCharm)

## Development Environment Setup

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd wtus-team-system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install backend dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

5. **Create an environment file**:
   Create a `.env` file in the backend directory with the following contents:
   ```
   SECRET_KEY=your_secret_key_here
   DATABASE_URI=sqlite:///wtus_team_system.db
   DEBUG=True
   ```

6. **Create uploads directory**:
   ```bash
   mkdir uploads
   ```

7. **Run the Flask development server**:
   ```bash
   python run.py
   ```
   The server will be available at http://localhost:5000.

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```
   The frontend will be available at http://localhost:3000.

## Production Deployment

### Backend Deployment

#### Option 1: Using Gunicorn with Nginx (Recommended for Linux servers)

1. **Install Gunicorn**:
   ```bash
   pip install gunicorn
   ```

2. **Create a Gunicorn service file** (for systemd-based Linux distributions):
   Create a file named `/etc/systemd/system/wtus-backend.service` with the following contents:
   ```ini
   [Unit]
   Description=WTUS Team System Backend
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/path/to/wtus-team-system/backend
   ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 run:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

3. **Set up Nginx as a reverse proxy**:
   Create a file named `/etc/nginx/sites-available/wtus-backend` with the following contents:
   ```nginx
   server {
       listen 80;
       server_name your_domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

4. **Enable the Nginx site**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/wtus-backend /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

5. **Start the backend service**:
   ```bash
   sudo systemctl start wtus-backend
   sudo systemctl enable wtus-backend
   ```

#### Option 2: Using Docker

1. **Create a Dockerfile** in the backend directory:
   ```dockerfile
   FROM python:3.10-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   RUN mkdir -p uploads

   ENV SECRET_KEY=your_secret_key_here
   ENV DATABASE_URI=sqlite:///wtus_team_system.db
   ENV DEBUG=False

   EXPOSE 5000

   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
   ```

2. **Build and run the Docker container**:
   ```bash
   docker build -t wtus-backend .
   docker run -d -p 5000:5000 wtus-backend
   ```

### Frontend Deployment

#### Option 1: Static File Hosting

1. **Build the React application**:
   ```bash
   cd frontend
   npm run build
   ```

2. **Configure Nginx to serve the static files**:
   Create a file named `/etc/nginx/sites-available/wtus-frontend` with the following contents:
   ```nginx
   server {
       listen 80;
       server_name your_frontend_domain.com;
       root /path/to/wtus-team-system/frontend/build;

       location / {
           try_files $uri /index.html;
       }
   }
   ```

3. **Enable the Nginx site**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/wtus-frontend /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

#### Option 2: Using Docker

1. **Create a Dockerfile** in the frontend directory:
   ```dockerfile
   FROM node:14 as build
   WORKDIR /app
   COPY package*.json ./
   RUN npm install
   COPY . .
   RUN npm run build

   FROM nginx:stable-alpine
   COPY --from=build /app/build /usr/share/nginx/html
   COPY nginx.conf /etc/nginx/conf.d/default.conf
   EXPOSE 80
   CMD ["nginx", "-g", "daemon off;"]
   ```

2. **Create an nginx.conf file**:
   ```nginx
   server {
       listen 80;
       server_name _;

       location / {
           root /usr/share/nginx/html;
           try_files $uri /index.html;
       }

       location /api {
           proxy_pass http://backend:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

3. **Build and run the Docker container**:
   ```bash
   docker build -t wtus-frontend .
   docker run -d -p 80:80 wtus-frontend
   ```

### Database Configuration

For production environments, consider using a more robust database system such as PostgreSQL or MySQL instead of SQLite.

#### PostgreSQL Setup

1. **Install PostgreSQL**:
   ```bash
   sudo apt-get update
   sudo apt-get install postgresql postgresql-contrib
   ```

2. **Create a database and user**:
   ```bash
   sudo -u postgres psql

   postgres=# CREATE DATABASE wtus_db;
   postgres=# CREATE USER wtus_user WITH PASSWORD 'your_strong_password';
   postgres=# GRANT ALL PRIVILEGES ON DATABASE wtus_db TO wtus_user;
   postgres=# \q
   ```

3. **Update the DATABASE_URI in your environment variables**:
   ```
   DATABASE_URI=postgresql://wtus_user:your_strong_password@localhost/wtus_db
   ```

## Environment-Specific Configurations

### Development
In development, use:
- Debug mode enabled
- SQLite database
- No HTTPS required

### Staging
In staging, use:
- Debug mode disabled
- Test database (can be SQLite or a proper DB system)
- HTTPS recommended

### Production
In production, use:
- Debug mode strictly disabled
- Production database (PostgreSQL or MySQL recommended)
- HTTPS required
- Proper logging configuration
- Regular backups

## Security Considerations

1. **Secret Key**:
   - Generate a strong, unique secret key for each environment
   - Never reuse secret keys between environments
   - Store secret keys securely, not in code repositories

2. **Environment Variables**:
   - Use environment variables for sensitive configuration
   - Never commit .env files to version control

3. **HTTPS**:
   - Always use HTTPS in production
   - Use Let's Encrypt for free SSL certificates
   - Configure proper SSL settings in Nginx

4. **Database Security**:
   - Use strong passwords for database users
   - Restrict database access to only necessary IP addresses
   - Regularly update database software

5. **File Uploads**:
   - Validate file types and sizes
   - Scan uploaded files for malware if possible
   - Store uploaded files outside the web root

## Monitoring and Maintenance

1. **Set up logging**:
   - Configure application logging
   - Review logs regularly

2. **Database backups**:
   - Set up regular automated backups
   - Test backup restoration periodically

3. **System updates**:
   - Keep all software up-to-date
   - Plan regular maintenance windows

4. **Performance monitoring**:
   - Monitor server resource usage
   - Set up alerts for unusual activity

## Troubleshooting

### Common Issues

1. **Backend fails to start**:
   - Check if the port is already in use
   - Verify that all dependencies are installed
   - Check for syntax errors in Python files

2. **Frontend fails to connect to backend**:
   - Verify that the backend is running
   - Check for CORS configuration issues
   - Verify API endpoint URLs

3. **Database connection issues**:
   - Verify database credentials
   - Check if the database server is running
   - Ensure network connectivity to the database

4. **File upload failures**:
   - Check file permissions on the uploads directory
   - Verify that the directory exists
   - Check file size limitations