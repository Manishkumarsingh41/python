# Student Details Program

# Define a dictionary to store student details
student = {
    "name": "",
    "age": 0,
    "grade": "",
    "major": "",
}

# Prompt the user for input and store it in the dictionary
student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter student age: "))
student["grade"] = input("Enter student grade: ")
student["Hobby"] = input("Enter student Hobby: ")

# Print out the student details
print("Student Details:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}")
print(f"Hobby: {student['Hobby']}")
