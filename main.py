import sqlite3
from database.db import insert_student, create_table, get_students, search_student, delete_student, update_student
create_table()
from models.student import Student
from file_handler import save_student, read_students

# create student
student1 = Student(1, "Akshaya", 95)

# save student to file
save_student(student1)

# read all students
students = read_students()

print("Student Records:")
for s in students:
    print(s)
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Sort by Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

       student_id = input("Enter Student ID: ")
       while True:
             name = input("Enter Student Name: ")
             if name.strip() != "":
                break
             else:
                print("Name cannot be empty!")
       #name = input("Enter Student Name: ")
       while True:
         try:
            marks = int(input("Enter Marks: "))
            break
         except ValueError:
            print("Marks must be a number!")
       #marks = input("Enter Marks: ")
       try:
            insert_student(student_id, name, marks)
            print("Student added successfully!")

       except sqlite3.IntegrityError:
               print("Student ID already exists!")
               #print("Student added successfully!")
    elif choice == "2":

         students = get_students()

         print("\nID\tName\tMarks")
         print("----------------------")
         for student in students:
            print(f"{student[0]}\t{student[1]}\t{student[2]}")
    elif choice == "3":
         search_id = input("Enter Student ID to search: ")

         students = search_student(search_id)
         if student:
                print("Student Found:")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Marks:", student[2])
         else:
             print("Student not found")
    elif choice == "4":
         delete_id = input("Enter Student ID to delete: ")

         delete_student(delete_id)

         print("Student deleted successfully")

    elif choice == "5":

         update_id = input("Enter Student ID to update: ")
         new_marks=input("Enter new marks: ")
         update_student(update_id, new_marks)


         print("Student updated successfully!")
    elif choice == "6":

         students = read_students()

         student_list = []

         for s in students:
             data = s.strip().split(",")
             student_list.append(data)

         student_list.sort(key=lambda x: int(x[2]), reverse=True)

         print("\nStudents Sorted by Marks")

         print("ID\tName\tMarks")
         print("----------------------")

         for student in student_list:
             print(f"{student[0]}\t{student[1]}\t{student[2]}")
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select from the menu.")
    
        