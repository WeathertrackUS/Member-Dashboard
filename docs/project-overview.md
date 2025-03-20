# WTUS Team System - Project Overview

## Introduction
The WTUS Team System is a collaborative platform designed for WeatherTrackUS team members to efficiently manage schedules, tasks, and share resources. This application facilitates coordination between team members with different specialties and enables smooth workflow management.

## Purpose
The primary purpose of this application is to:
- Streamline team scheduling and availability tracking
- Facilitate task assignment and progress monitoring
- Provide a centralized system for file sharing and resource management
- Enable communication through task-specific discussion boards

## Technical Stack
The application uses a modern tech stack split between frontend and backend:

### Frontend
- **Framework**: React.js
- **Routing**: React Router
- **Styling**: Custom CSS

### Backend
- **Framework**: Flask (Python)
- **Database**: SQLite (as indicated by configuration)
- **Authentication**: Custom authentication system

## System Architecture
The system follows a client-server architecture:
- **Frontend**: Single-page application built with React
- **Backend**: RESTful API built with Flask
- **Database**: SQLite database for data persistence
- **File Storage**: Local file system for storing uploadable/downloadable assets

## Key Features
1. **User Availability Management**
   - Calendar interface for availability input
   - Team schedule visualization
   
2. **Task Management**
   - Task creation, assignment, and status tracking
   - Categorization with labels
   - Due date management
   - Discussion/comment functionality for each task
   
3. **File Management**
   - Upload/download functionality
   - File categorization and search
   - Support for various file formats, especially design files (.psd)

## Current Project Status
The project currently has the basic structure in place with:
- Core frontend components defined
- Backend API routes established
- Basic data models created
- Authentication system implemented

Further development is ongoing to enhance functionality and user experience.