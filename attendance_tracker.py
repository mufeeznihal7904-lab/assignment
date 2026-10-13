
import csv
import os

FILE_NAME = "attendance.csv"


# Load attendance records from CSV file
def load_records():
    records = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                records[row["Name"]] = row["Attendance"]

    return records


# Save attendance records to CSV file
def save_records(records):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Attendance"])

        for name, status in records.items():
            writer.writerow([name, status])


# Display attendance list
def display_attendance(records):
    if not records:
        print("No attendance records found.")
        return

    print("\n--- Student Attendance List ---")
    for name, status in records.items():
        print(name, "-", status)


# Calculate attendance percentage
def calculate_percentage(records):
    if not records:
        print("No attendance records available.")
        return

    total = len(records)
    present = sum(
        1 for status in records.values() if status == "Present"
    )

    percentage = (present / total) * 100

    print("Total Students:", total)
    print("Present Students:", present)
    print("Absent Students:", total - present)
    print(f"Attendance Percentage: {percentage:.2f}%")


records = load_records()

while True:
    print("\n--- Student Attendance Tracker ---")
    print("1. Add Student Attendance")
    print("2. Display Attendance")
    print("3. Calculate Attendance Percentage")
    print("4. Save Records")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            continue

        status = input("Enter attendance (P/A): ").strip().upper()

        if status == "P":
            records[name] = "Present"
            print("Marked as Present.")
        elif status == "A":
            records[name] = "Absent"
            print("Marked as Absent.")
        else:
            print("Invalid input. Enter P or A.")
            continue

        save_records(records)

    elif choice == "2":
        display_attendance(records)

    elif choice == "3":
        calculate_percentage(records)

    elif choice == "4":
        save_records(records)
        print("Attendance records saved successfully.")

    elif choice == "5":
        save_records(records)
        print("Records saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")