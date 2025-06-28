import json

# Load the student.json file into a Python list using json.load()
with open('student.json', 'r') as file:
    students = json.load(file)

# Function to print each student in the required format
def print_students(data):
    for student in data:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Step 1: Notify user and print original list
print("=== Original Student List ===")
print_students(students)

# Step 2: Append your fictional info
students.append({
    "F_Name": "Sylvester",
    "L_Name": "Brandon",
    "Student_ID": 21448053,
    "Email": "sbrandon@my365.bellevue.edu"
})

# Step 3: Notify user and print updated list
print("\n=== Updated Student List ===")
print_students(students)

# Step 4: Save the updated list back to student.json using json.dump()
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

# Step 5: Notify user that file was updated
print("\nThe student.json file has been updated.")