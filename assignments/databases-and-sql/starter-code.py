import sqlite3
import sys
from datetime import datetime
from pathlib import Path


class StudentDatabase:
    def __init__(self, db_file="students.db"):
        """Initialize database connection and create tables if needed."""
        self.db_file = db_file
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()

    def connect(self):
        """Establish database connection."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
            print(f"Connected to database: {self.db_file}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit(1)

    def create_tables(self):
        """Create database tables if they don't exist."""
        try:
            self.cursor.executescript(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    enrolledDate TEXT DEFAULT CURRENT_DATE
                );

                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    code TEXT UNIQUE NOT NULL,
                    credits INTEGER DEFAULT 3
                );

                CREATE TABLE IF NOT EXISTS enrollments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    studentId INTEGER NOT NULL,
                    courseId INTEGER NOT NULL,
                    grade REAL,
                    enrollmentDate TEXT DEFAULT CURRENT_DATE,
                    FOREIGN KEY (studentId) REFERENCES students(id),
                    FOREIGN KEY (courseId) REFERENCES courses(id)
                );
            """
            )
            self.conn.commit()
            print("Database tables ready.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_student(self, name, email):
        """Add a new student."""
        try:
            self.cursor.execute(
                "INSERT INTO students (name, email) VALUES (?, ?)", (name, email)
            )
            self.conn.commit()
            print(f"Student '{name}' added successfully.")
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Error: Student with email '{email}' already exists.")
            return None

    def add_course(self, name, code, credits=3):
        """Add a new course."""
        try:
            self.cursor.execute(
                "INSERT INTO courses (name, code, credits) VALUES (?, ?, ?)",
                (name, code, credits),
            )
            self.conn.commit()
            print(f"Course '{name}' ({code}) added successfully.")
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Error: Course with code '{code}' already exists.")
            return None

    def enroll_student(self, student_id, course_id, grade=None):
        """Enroll a student in a course."""
        try:
            self.cursor.execute(
                "INSERT INTO enrollments (studentId, courseId, grade) VALUES (?, ?, ?)",
                (student_id, course_id, grade),
            )
            self.conn.commit()
            print(f"Student {student_id} enrolled in course {course_id}.")
        except sqlite3.Error as e:
            print(f"Error enrolling student: {e}")

    def list_students(self):
        """List all students."""
        try:
            self.cursor.execute("SELECT id, name, email, enrolledDate FROM students")
            students = self.cursor.fetchall()
            if students:
                print("\n--- All Students ---")
                print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Enrolled':<12}")
                print("-" * 65)
                for student in students:
                    print(
                        f"{student[0]:<5} {student[1]:<20} {student[2]:<25} {student[3]:<12}"
                    )
            else:
                print("No students found.")
        except sqlite3.Error as e:
            print(f"Error listing students: {e}")

    def list_courses(self):
        """List all courses."""
        try:
            self.cursor.execute("SELECT id, name, code, credits FROM courses")
            courses = self.cursor.fetchall()
            if courses:
                print("\n--- All Courses ---")
                print(f"{'ID':<5} {'Name':<25} {'Code':<10} {'Credits':<8}")
                print("-" * 50)
                for course in courses:
                    print(
                        f"{course[0]:<5} {course[1]:<25} {course[2]:<10} {course[3]:<8}"
                    )
            else:
                print("No courses found.")
        except sqlite3.Error as e:
            print(f"Error listing courses: {e}")

    def students_in_course(self, course_code):
        """List all students enrolled in a specific course."""
        try:
            self.cursor.execute(
                """
                SELECT s.id, s.name, s.email, e.grade
                FROM students s
                JOIN enrollments e ON s.id = e.studentId
                JOIN courses c ON e.courseId = c.id
                WHERE c.code = ?
                """,
                (course_code,),
            )
            results = self.cursor.fetchall()
            if results:
                print(f"\n--- Students in Course {course_code} ---")
                print(f"{'Student ID':<12} {'Name':<20} {'Email':<25} {'Grade':<8}")
                print("-" * 65)
                for result in results:
                    grade = f"{result[3]:.1f}" if result[3] else "N/A"
                    print(
                        f"{result[0]:<12} {result[1]:<20} {result[2]:<25} {grade:<8}"
                    )
            else:
                print(f"No students enrolled in course {course_code}.")
        except sqlite3.Error as e:
            print(f"Error querying students: {e}")

    def student_profile(self, student_id):
        """Display complete profile for a student."""
        try:
            self.cursor.execute(
                "SELECT name, email, enrolledDate FROM students WHERE id = ?",
                (student_id,),
            )
            student = self.cursor.fetchone()
            if not student:
                print(f"Student {student_id} not found.")
                return

            print(f"\n--- Student Profile (ID: {student_id}) ---")
            print(f"Name: {student[0]}")
            print(f"Email: {student[1]}")
            print(f"Enrolled: {student[2]}")

            self.cursor.execute(
                """
                SELECT c.name, c.code, e.grade, e.enrollmentDate
                FROM enrollments e
                JOIN courses c ON e.courseId = c.id
                WHERE e.studentId = ?
                """,
                (student_id,),
            )
            enrollments = self.cursor.fetchall()
            if enrollments:
                print("\nCourses:")
                for enrollment in enrollments:
                    grade = f"{enrollment[2]:.1f}" if enrollment[2] else "N/A"
                    print(
                        f"  - {enrollment[1]}: {enrollment[0]} (Grade: {grade})"
                    )
            else:
                print("No course enrollments.")
        except sqlite3.Error as e:
            print(f"Error fetching profile: {e}")

    def course_statistics(self, course_code):
        """Display statistics for a course."""
        try:
            self.cursor.execute(
                """
                SELECT COUNT(*) as enrollment_count, AVG(grade) as avg_grade
                FROM enrollments e
                JOIN courses c ON e.courseId = c.id
                WHERE c.code = ? AND e.grade IS NOT NULL
                """,
                (course_code,),
            )
            result = self.cursor.fetchone()
            if result and result[0] > 0:
                print(f"\n--- Statistics for Course {course_code} ---")
                print(f"Total Enrollments: {result[0]}")
                print(f"Average Grade: {result[1]:.2f}")
            else:
                print(f"No grade data available for course {course_code}.")
        except sqlite3.Error as e:
            print(f"Error calculating statistics: {e}")

    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")


def main():
    db = StudentDatabase()

    # Sample data insertion
    print("\n--- Initializing Sample Data ---")
    sid1 = db.add_student("Alice Johnson", "alice@example.com")
    sid2 = db.add_student("Bob Smith", "bob@example.com")
    sid3 = db.add_student("Charlie Brown", "charlie@example.com")

    cid1 = db.add_course("Python Programming", "CS101", 4)
    cid2 = db.add_course("Web Development", "CS102", 3)
    cid3 = db.add_course("Database Design", "CS103", 3)

    # Enroll students
    if sid1 and cid1:
        db.enroll_student(sid1, cid1, 95)
    if sid1 and cid2:
        db.enroll_student(sid1, cid2, 88)
    if sid2 and cid1:
        db.enroll_student(sid2, cid1, 92)
    if sid3 and cid3:
        db.enroll_student(sid3, cid3, 87)

    # Display information
    print("\n--- Database Contents ---")
    db.list_students()
    db.list_courses()

    # Run queries
    print("\n--- Query Examples ---")
    db.students_in_course("CS101")
    db.student_profile(sid1)
    db.course_statistics("CS101")

    db.close()


if __name__ == "__main__":
    main()
