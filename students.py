from pathlib import Path
import json
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class Student:
    name: str
    list_number: int
    grade: float

    def __str__(self) -> str:
        return f"Name: {self.name}, List Number: {self.list_number}, Grade: {self.grade}"

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Student":
        return cls(name=d["name"], list_number=d["list_number"], grade=d["grade"])


_desktop = Path.home() / "Desktop"
if not _desktop.exists():
    _desktop = Path.home()
file_path = _desktop / "students.json"

students: List[Student] = []

def load_students() -> None:
    global students
    if file_path.exists():
        try:
            data = json.loads(file_path.read_text(encoding="utf-8") or "[]")
            students = [Student.from_dict(d) for d in data]
            print("Students loaded successfully.")
        except Exception as e:
            print(f"Failed to load students: {e}")

def save_students() -> None:
    try:
        data = [s.to_dict() for s in students]
        file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Students saved successfully.")
    except Exception as e:
        print(f"Failed to save students: {e}")

def add_student() -> None:
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        list_number = int(input("Enter list number: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    if any(s.list_number == list_number for s in students):
        print("A student with this list number already exists.")
        return

    try:
        grade = float(input("Enter grade: ").strip())
    except ValueError:
        print("Please enter a valid grade.")
        return

    students.append(Student(name=name, list_number=list_number, grade=grade))
    print("Student added successfully.")

def view_students() -> None:
    if not students:
        print("No students available.")
        return
    for s in students:
        print(s)

def search_student_by_list_number(list_number: int) -> Optional[Student]:
    for s in students:
        if s.list_number == list_number:
            return s
    return None

def search_and_display_student() -> None:
    try:
        list_number = int(input("Enter list number: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    student = search_student_by_list_number(list_number)
    if student:
        print(student)
    else:
        print("Student with entered list number doesn't exist.")

def change_student_grade() -> None:
    try:
        list_number = int(input("Enter student list number: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        new_grade = float(input("Enter new grade: ").strip())
    except ValueError:
        print("Please enter a valid grade.")
        return

    student = search_student_by_list_number(list_number)
    if student:
        student.grade = new_grade
        print("Grade changed successfully.")
    else:
        print("Student with entered list number doesn't exist.")

def main() -> None:
    load_students()
    while True:
        print()
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by list number")
        print("4. Update student grade")
        print("5. Save")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        try:
            opt = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if opt == 1:
            add_student()
        elif opt == 2:
            view_students()
        elif opt == 3:
            search_and_display_student()
        elif opt == 4:
            change_student_grade()
        elif opt == 5:
            save_students()
        elif opt == 6:
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")