# 📘 Assignment: Data Structures in Python

## 🎯 Objective

Build a solid understanding of Python's core data structures—lists, dictionaries, sets, and tuples—by implementing a practical application that uses multiple structures together.

## 📝 Tasks

### 🛠️ Implement a Student Grade Management System

#### Description
Create a Python application that manages student records using dictionaries, lists, sets, and tuples. The system should store student information, track grades, calculate statistics, and allow searching and filtering operations.

#### Requirements
Completed program should:

- Use dictionaries to store student records (name, ID, grades).
- Use lists to maintain ordered collections of students.
- Use sets to track unique subject names and unique student IDs.
- Use tuples to store immutable grade entries (subject, grade, date).
- Implement functions to:
  - Add and remove students.
  - Record grades for students in different subjects.
  - Calculate average grade per student and per subject.
  - Find students with grades in a specific range.
  - Search students by name, ID, or subject.
  - Display reports sorted by grade, name, or ID.
- Demonstrate the difference between data structures through practical use cases.
- Handle duplicate entries and invalid data gracefully.

Example usage:

```python
system = GradeManagementSystem()
system.add_student("Alice", 101)
system.add_student("Bob", 102)
system.record_grade(101, "Math", 95)
system.record_grade(101, "Science", 88)
print(system.get_average(101))  # Output: 91.5
print(system.get_students_by_subject("Math"))
```

Starter code: see `starter-code.py` in this folder.
