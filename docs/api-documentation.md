# API Documentation

## Overview
This document provides detailed information about the RESTful API endpoints available in the WTUS Team System. Each section describes the endpoints for a specific resource, including request methods, URL parameters, request body format, and response format.

## Base URL
All API endpoints are relative to the base URL of your deployment. For local development, this is typically:
```
http://localhost:5000
```

## Authentication Endpoints

### Register User
Creates a new user account.

- **URL**: `/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "johndoe",
    "password": "secure_password",
    "email": "john.doe@example.com"
  }
  ```
- **Success Response**:
  - **Code**: 201 Created
  - **Content**:
    ```json
    {
      "message": "User registered successfully."
    }
    ```
- **Error Response**:
  - **Code**: 400 Bad Request
  - **Content**:
    ```json
    {
      "message": "Username and password are required."
    }
    ```

### Login
Authenticates a user and provides an access token.

- **URL**: `/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "johndoe",
    "password": "secure_password"
  }
  ```
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    {
      "message": "Login successful."
    }
    ```
- **Error Response**:
  - **Code**: 401 Unauthorized
  - **Content**:
    ```json
    {
      "message": "Invalid username or password."
    }
    ```

## Task Endpoints

### Get All Tasks
Retrieves a list of all tasks.

- **URL**: `/tasks`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    [
      {
        "id": 1,
        "title": "Update weather graphics",
        "description": "Create new icons for the severe weather system",
        "status": "In Progress",
        "due_date": "2025-04-15",
        "assigned_to": 3,
        "comments": [
          "First draft completed",
          "Needs more contrast on thunderstorm icons"
        ]
      },
      {
        "id": 2,
        "title": "Twitter post for storm system",
        "description": "Create a tweet about the incoming storm system",
        "status": "Pending",
        "due_date": "2025-03-25",
        "assigned_to": 2,
        "comments": []
      }
    ]
    ```

### Create Task
Creates a new task.

- **URL**: `/tasks`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "Radar loop creation",
    "description": "Create radar loop for website front page",
    "status": "Pending",
    "due_date": "2025-04-01",
    "assigned_to": 3
  }
  ```
- **Success Response**:
  - **Code**: 201 Created
  - **Content**:
    ```json
    {
      "id": 3,
      "title": "Radar loop creation",
      "description": "Create radar loop for website front page",
      "status": "Pending",
      "due_date": "2025-04-01",
      "assigned_to": 3,
      "comments": []
    }
    ```

### Update Task
Updates an existing task.

- **URL**: `/tasks/<task_id>`
- **Method**: `PUT`
- **URL Parameters**:
  - `task_id`: ID of the task to update
- **Request Body**:
  ```json
  {
    "status": "In Progress",
    "due_date": "2025-04-05"
  }
  ```
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    {
      "id": 3,
      "title": "Radar loop creation",
      "description": "Create radar loop for website front page",
      "status": "In Progress",
      "due_date": "2025-04-05",
      "assigned_to": 3,
      "comments": []
    }
    ```
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**:
    ```json
    {
      "message": "Task not found"
    }
    ```

### Delete Task
Deletes a task.

- **URL**: `/tasks/<task_id>`
- **Method**: `DELETE`
- **URL Parameters**:
  - `task_id`: ID of the task to delete
- **Success Response**:
  - **Code**: 204 No Content
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**:
    ```json
    {
      "message": "Task not found"
    }
    ```

## Schedule Endpoints

### Get All Schedules
Retrieves all schedules.

- **URL**: `/schedules`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    [
      {
        "id": 1,
        "user_id": 2,
        "availability": [
          {"day_of_week": 1, "start_time": "09:00", "end_time": "17:00"},
          {"day_of_week": 2, "start_time": "09:00", "end_time": "17:00"},
          {"day_of_week": 3, "start_time": "09:00", "end_time": "17:00"}
        ]
      },
      {
        "id": 2,
        "user_id": 3,
        "availability": [
          {"day_of_week": 1, "start_time": "12:00", "end_time": "20:00"},
          {"day_of_week": 2, "start_time": "12:00", "end_time": "20:00"},
          {"day_of_week": 4, "start_time": "09:00", "end_time": "17:00"}
        ]
      }
    ]
    ```

### Get User Schedule
Retrieves the schedule for a specific user.

- **URL**: `/schedules/<user_id>`
- **Method**: `GET`
- **URL Parameters**:
  - `user_id`: ID of the user
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    {
      "id": 1,
      "user_id": 2,
      "availability": [
        {"day_of_week": 1, "start_time": "09:00", "end_time": "17:00"},
        {"day_of_week": 2, "start_time": "09:00", "end_time": "17:00"},
        {"day_of_week": 3, "start_time": "09:00", "end_time": "17:00"}
      ]
    }
    ```
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**:
    ```json
    {
      "message": "Schedule not found for user"
    }
    ```

### Create Schedule
Creates a new schedule.

- **URL**: `/schedules`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "user_id": 4,
    "availability": [
      {"day_of_week": 1, "start_time": "10:00", "end_time": "18:00"},
      {"day_of_week": 3, "start_time": "10:00", "end_time": "18:00"},
      {"day_of_week": 5, "start_time": "10:00", "end_time": "18:00"}
    ]
  }
  ```
- **Success Response**:
  - **Code**: 201 Created
  - **Content**:
    ```json
    {
      "id": 3,
      "user_id": 4,
      "availability": [
        {"day_of_week": 1, "start_time": "10:00", "end_time": "18:00"},
        {"day_of_week": 3, "start_time": "10:00", "end_time": "18:00"},
        {"day_of_week": 5, "start_time": "10:00", "end_time": "18:00"}
      ]
    }
    ```

### Update Schedule
Updates an existing schedule.

- **URL**: `/schedules/<schedule_id>`
- **Method**: `PUT`
- **URL Parameters**:
  - `schedule_id`: ID of the schedule to update
- **Request Body**:
  ```json
  {
    "availability": [
      {"day_of_week": 1, "start_time": "09:00", "end_time": "17:00"},
      {"day_of_week": 2, "start_time": "09:00", "end_time": "17:00"}
    ]
  }
  ```
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    {
      "id": 3,
      "user_id": 4,
      "availability": [
        {"day_of_week": 1, "start_time": "09:00", "end_time": "17:00"},
        {"day_of_week": 2, "start_time": "09:00", "end_time": "17:00"}
      ]
    }
    ```
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**:
    ```json
    {
      "message": "Schedule not found"
    }
    ```

### Delete Schedule
Deletes a schedule.

- **URL**: `/schedules/<schedule_id>`
- **Method**: `DELETE`
- **URL Parameters**:
  - `schedule_id`: ID of the schedule to delete
- **Success Response**:
  - **Code**: 204 No Content
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**:
    ```json
    {
      "message": "Schedule not found"
    }
    ```

## Asset Endpoints

### List Assets
Lists all available files.

- **URL**: `/assets`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    [
      "severe-weather-map.jpg",
      "radar-template.psd",
      "storm-icons.psd",
      "tornado-warning-template.png"
    ]
    ```
- **Error Response**:
  - **Code**: 500 Internal Server Error
  - **Content**:
    ```json
    {
      "error": "Unable to access asset directory"
    }
    ```

### Download Asset
Downloads a specific file.

- **URL**: `/assets/<filename>`
- **Method**: `GET`
- **URL Parameters**:
  - `filename`: Name of the file to download
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: The requested file as an attachment
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**:
    ```json
    {
      "error": "File not found"
    }
    ```

## Error Handling
All API endpoints follow a consistent error handling pattern:

- **400 Bad Request**: When the request is malformed or missing required parameters
- **401 Unauthorized**: When authentication is required but not provided or invalid
- **403 Forbidden**: When the user doesn't have permission to access a resource
- **404 Not Found**: When the requested resource doesn't exist
- **500 Internal Server Error**: When an unexpected error occurs on the server

Error responses always include a message field that describes the error.

## Rate Limiting
The API currently does not implement rate limiting, but this may be added in future versions.