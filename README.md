# Student Record Management System

A Python-based application to manage student records using SQLite database.

## Technologies Used
- Python
- Flask
- SQLite
- HTML


## Live Demo
https://akshhhh.pythonanywhere.com

## Features
- Add Student
- View Students
- Search Student
- Update Student Marks
- Delete Student
- Input Validation
- Database Timestamp Tracking

## Project Structure
student-record-management-system
│
├── main.py
├── app.py
├── database
│   └── db.py
├── models
│   └── student.py
├── templates
│   └── index.html
├── students.db
└── README.md

## Database Schema

```mermaid
erDiagram

    STUDENTS {
        VARCHAR id PK
        VARCHAR name
        INT marks
        TIMESTAMP created_at
        BOOLEAN is_deleted
    }

    AUDIT_LOGS {
        INT log_id PK
        VARCHAR action_type
        VARCHAR student_id FK
        TIMESTAMP action_time
    }

    USERS {
        INT user_id PK
        VARCHAR username
        VARCHAR role
    }

    STUDENTS ||--o{ AUDIT_LOGS : generates
```
