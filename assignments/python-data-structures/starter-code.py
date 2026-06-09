from typing import Dict, List, Set, Tuple
from datetime import datetime


class GradeManagementSystem:
    def __init__(self):
        # Using different data structures for different purposes
        self.students: Dict[int, Dict] = {}  # id -> {name, grades}
        self.student_ids: Set[int] = set()  # unique student IDs
        self.student_list: List[int] = []  # ordered list of student IDs
        self.subjects: Set[str] = set()  # unique subjects

    def add_student(self, name: str, student_id: int) -> bool:
        """Add a new student."""
        if student_id in self.student_ids:
            print(f"Student ID {student_id} already exists.")
            return False

        self.students[student_id] = {"name": name, "grades": []}
        self.student_ids.add(student_id)
        self.student_list.append(student_id)
        return True

    def record_grade(self, student_id: int, subject: str, grade: float) -> bool:
        """Record a grade for a student. Grade is stored as a tuple."""
        if student_id not in self.student_ids:
            print(f"Student ID {student_id} not found.")
            return False

        grade_entry: Tuple[str, float, str] = (
            subject,
            grade,
            datetime.now().strftime("%Y-%m-%d"),
        )
        self.students[student_id]["grades"].append(grade_entry)
        self.subjects.add(subject)
        return True

    def get_average(self, student_id: int) -> float:
        """Calculate average grade for a student."""
        if student_id not in self.student_ids:
            return 0.0

        grades = self.students[student_id]["grades"]
        if not grades:
            return 0.0

        total = sum(grade[1] for grade in grades)
        return round(total / len(grades), 2)

    def get_subject_average(self, subject: str) -> float:
        """Calculate average grade for a subject across all students."""
        grades = []
        for student_id in self.student_list:
            for grade_entry in self.students[student_id]["grades"]:
                if grade_entry[0] == subject:
                    grades.append(grade_entry[1])

        if not grades:
            return 0.0

        return round(sum(grades) / len(grades), 2)

    def find_by_grade_range(self, min_grade: float, max_grade: float) -> List[int]:
        """Find students with average grade in a specific range."""
        result = []
        for student_id in self.student_list:
            avg = self.get_average(student_id)
            if min_grade <= avg <= max_grade:
                result.append(student_id)
        return result

    def get_students_by_subject(self, subject: str) -> List[str]:
        """Get list of students who have grades in a specific subject."""
        result = []
        for student_id in self.student_list:
            for grade_entry in self.students[student_id]["grades"]:
                if grade_entry[0] == subject and student_id not in result:
                    result.append(self.students[student_id]["name"])
        return result

    def remove_student(self, student_id: int) -> bool:
        """Remove a student."""
        if student_id not in self.student_ids:
            return False

        del self.students[student_id]
        self.student_ids.discard(student_id)
        self.student_list.remove(student_id)
        return True

    def display_all_students(self) -> None:
        """Display all students and their averages."""
        print(f"\n{'ID':<8} {'Name':<20} {'Average':<10}")
        print("-" * 40)
        for student_id in self.student_list:
            student = self.students[student_id]
            avg = self.get_average(student_id)
            print(f"{student_id:<8} {student['name']:<20} {avg:<10.2f}")


# Example usage
if __name__ == "__main__":
    system = GradeManagementSystem()

    # Add students
    system.add_student("Alice", 101)
    system.add_student("Bob", 102)
    system.add_student("Charlie", 103)

    # Record grades
    system.record_grade(101, "Math", 95)
    system.record_grade(101, "Science", 88)
    system.record_grade(102, "Math", 92)
    system.record_grade(102, "Science", 85)
    system.record_grade(103, "Math", 78)

    # Display all students
    system.display_all_students()

    # Show statistics
    print("\nSubject Averages:")
    print(f"  Math: {system.get_subject_average('Math')}")
    print(f"  Science: {system.get_subject_average('Science')}")

    print("\nStudents with grades 85-95:")
    print(system.find_by_grade_range(85, 95))
