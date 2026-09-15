students = {}

def grade(p):
    if p >= 90: return "A+"
    if p >= 80: return "A"
    if p >= 70: return "B"
    if p >= 60: return "C"
    if p >= 50: return "D"
    if p >= 40: return "E"
    return "F"

def percentage(marks):
    return sum(marks.values()) / len(marks)

def add_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Student aists.")
        return

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    cls = input("Enter class: ")
    section = input("Enter section: ")

    marks = {}
    for subject in ["English", "Maths", "Science", "Computer", "Social Science"]:
        marks[subject] = float(input(f"Enter {subject} marks: "))

    students[roll] = {
        "name": name,
        "age": age,
        "class": cls,
        "section": section,
        "marks": marks
    }

    print("Student added successfully.")

def show_student(roll):
    s = students[roll]
    p = percentage(s["marks"])

    print("\nRoll Number:", roll)
    print("Name:", s["name"])
    print("Age:", s["age"])
    print("Class:", s["class"])
    print("Section:", s["section"])

    print("\nMarks:")
    for subject, mark in s["marks"].items():
        print(subject, ":", mark)

    print("Percentage:", round(p, 2), "%")
    print("Grade:", grade(p))
    print("Result:", "PASS" if p >= 40 else "FAIL")

def show_all():
    if not students:
        print("No students found.")
        return

    for roll in students:
        print("\n--------------------")
        show_student(roll)

def search_student():
    roll = input("Enter roll number: ")

    if roll in students:
        show_student(roll)
    else:
        print("Student not found.")

def update_marks():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    subjects = list(students[roll]["marks"])

    for i, subject in enumerate(subjects, 1):
        print(i, subject)

    choice = int(input("Choose subject: "))

    if 1 <= choice <= len(subjects):
        subject = subjects[choice - 1]
        mark = float(input("Enter new marks: "))

        if 0 <= mark <= 100:
            students[roll]["marks"][subject] = mark
            print("Marks updated.")
        else:
            print("Invalid marks.")
    else:
        print("Invalid choice.")

def delete_student():
    roll = input("Enter roll number: ")

    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

def topper():
    if not students:
        print("No students found.")
        return

    roll = max(
        students,
        key=lambda r: percentage(students[r]["marks"])
    )

    print("\nTopper:")
    show_student(roll)

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            topper()
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
