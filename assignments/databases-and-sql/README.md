# 📘 Assignment: Databases & SQL

## 🎯 Objective

Master database design and SQL queries by building a simple application that persists, queries, and manages data using SQLite.

## 📝 Tasks

### 🛠️ Build a Student Database Management Application

#### Description
Create a Python application using SQLite to manage student records with course enrollments. The application should allow users to create tables, insert records, query data with various filters, update records, and generate reports. This bridges the gap between in-memory data structures and real persistent storage.

#### Requirements
Completed program should:

- Create a SQLite database with at least 3 related tables (e.g., students, courses, enrollments).
- Implement CRUD operations (Create, Read, Update, Delete) for each table.
- Use proper SQL queries including:
  - Simple SELECT with WHERE conditions.
  - JOINs to query related data across multiple tables.
  - Aggregate functions (COUNT, AVG, SUM, MAX, MIN).
  - GROUP BY and ORDER BY clauses.
- Validate data before inserting (e.g., email format, enrollment constraints).
- Handle database errors gracefully (e.g., duplicate entries, foreign key violations).
- Provide a command-line interface to interact with the database.
- Generate reports such as:
  - List all students in a course
  - Calculate average grade per student
  - Find courses with the most enrollments
  - Display complete student profiles with all enrollments
- Use parameterized queries to prevent SQL injection.
- Include sample data for testing.

Example usage:

```bash
python starter-code.py --action enroll --student 101 --course C101
python starter-code.py --action report --type "students_in_course" --course C101
python starter-code.py --action list_students
```

Database schema overview:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    enrolledDate TEXT
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    code TEXT UNIQUE,
    credits INTEGER
);

CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    studentId INTEGER,
    courseId INTEGER,
    grade REAL,
    FOREIGN KEY (studentId) REFERENCES students(id),
    FOREIGN KEY (courseId) REFERENCES courses(id)
);
```

Starter code: see `starter-code.py` in this folder.
