import json
import os

DATA_FILE = "data/students.json"

# Ensure data folder and file exist
os.makedirs("data", exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    year = input("Enter Year: ")

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "year": year
    }

    data.append(student)
    save_data(data)
    print("Student added successfully!\n")


def view_students():
    data = load_data()
    if not data:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for s in data:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Course: {s['course']} | Year: {s['year']}")
    print()


def search_student():
    data = load_data()
    roll = input("Enter Roll Number to search: ")

    for s in data:
        if s['roll'] == roll:
            print("\n--- Student Found ---")
            print(f"Roll: {s['roll']}\nName: {s['name']}\nCourse: {s['course']}\nYear: {s['year']}\n")
            return

    print("Student not found.\n")


def delete_student():
    data = load_data()
    roll = input("Enter Roll Number to delete: ")

    new_data = [s for s in data if s['roll'] != roll]

    if len(new_data) == len(data):
        print("Student not found.\n")
    else:
        save_data(new_data)
        print("Student deleted successfully!\n")


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
