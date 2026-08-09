class Student:
     def __init__(self, name, roll_no, marks):
          self.name = name
          self.roll_no = roll_no
          self.marks = marks

students = []
def add_student(students):
     name = input("Enter your name: ")
     roll_no = int(input("Enetr your roll number: "))
     subjects = ["Maths", "Science", "English", "French", "Social Studies"]
     marks = {}
     for subject in subjects:
          marks[subject]= int(input(f"Enter marks for {subject}: "))
     
     s = Student(name, roll_no , marks)
     students.append(s)

def view(students):
     print(f"{'Name' :<10}{'Roll No.' :<15}{'Marks' :<15}")
     for student in students:
          print(f"{student.name :<10} {student.roll_no:<8} {student.marks}")

def search(students):
     roll_no = int(input("Enter the roll no u want to search: "))
     found = False
     for student in students:
          if roll_no == student.roll_no:
               print(f"Name: {student.name}")
               print(f"Roll No.- {student.roll_no}")
               print(student.marks)
               found = True
     if not found:
               print("STUDENT NOT FOUND")

def update(students):
     roll_no = int(input("Enter the roll no u want to search: "))
     found = False
     for student in students:
          if roll_no == student.roll_no:
               found = True
               print("1. Update name")
               print("2. Update marks")
               choice = int(input("What do u want to update(1-2): "))
               if choice == 1:
                    new_name = input("Enter updated name: ")
                    student.name = new_name
                    print("NAME UPDATED SUCCESSFULLY!")
               elif choice == 2:
                    print("Current Marks: ", student.marks)
                    subject = input("Enter the subject whose marks u want to update: ")
                    if subject in student.marks:
                         new_marks = int(input(f"Enter new marks for {subject}: "))
                         student.marks[subject] = new_marks
                         print("MARKS UPDATED SUCCESSFULLY!")
                    else:
                         print("SUBJECT NOT FOUND")
     if not found:
          print("STUDENT NOT FOUND")

def delete(students):
     roll_no = int(input("Enter the roll no. u want to delete: "))
     found = False
     for student in students:
          if roll_no == student.roll_no:
               students.remove(student)
               print("Student deleted successfully!")
               found = True
     if not found:
               print("STUDENT NOT FOUND")

while True:
     print()
     print("\n----- MENU -----")
     print("1. Add a new Student")
     print("2. View all student details")
     print("3. Search for student")
     print("4. Update student details")
     print("5. Delete a student")
     print("6. Exit")

     ch = int(input("Enter your choice: (1-6):"))

     if ch == 1:
          add_student(students)
     elif ch == 2:
          view(students)
     elif ch == 3:
          search(students)
     elif ch == 4:
          update(students)
     elif ch == 5:
          delete(students)
     elif ch == 6:
          print("---- THE END ----")
          break
     else:
          print("Invalid")

         