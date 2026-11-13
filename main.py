# Teacher's RankBoard - For Teachers to Manage Class Marks
# B.Tech 1st Year, VJIT

students = []
subjects = ["Maths", "Physics", "Python", "Chemistry", "English"]

print("Welcome to Teacher's RankBoard!")
print("Helping teachers manage class marks easily.")
n = int(input("How many number of student marks you want to enter? "))

for i in range(n):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter the name of the student : ")

    marks = []
    for sub in subjects:
        m = int(input(f"Enter marks for {sub}: "))
        marks.append(m)

    students.append([name, marks])

print("\nAll Students marks  are Added!")

def show_all():
    print("\n--- ALL MARKS ---")
    for student in students:
        name = student[0]
        marks = student[1]
        print(f"\n{name} marks:")
        for j in range(len(subjects)):
            print(f"  {subjects[j]} - {marks[j]}")

def show_average():
    print("\n--- AVERAGE OF ALL STUDENTS ---")
    for student in students:
        name = student[0]
        marks = student[1]
        avg = sum(marks) / len(marks)
        print(f"{name} - Average: {avg:.1f}")

def show_rank1():
    rank1_name = ""
    rank1_avg = -1

    for student in students:
        name = student[0]
        marks = student[1]
        avg = sum(marks) / len(marks)
        if avg > rank1_avg:
            rank1_avg = avg
            rank1_name = name

    print(f"\nRANK 1 STUDENT IS: {rank1_name} with {rank1_avg:.1f} average!")

def change_mark():
    show_all()
    name = input("\nWhose marks to change? ")
    sub = input("Which subject? ")

    for student in students:
        if student[0] == name:
            if sub in subjects:
                pos = subjects.index(sub)
                new_val = int(input(f"Enter new marks for {sub}: "))
                student[1][pos] = new_val
                print("Changed!")
                return
    print("Student or Subject not found!")

def add_student():
    name = input("Enter new student name: ")
    marks = []
    for sub in subjects:
        m = int(input(f"Enter marks for {sub}: "))
        marks.append(m)
    students.append([name, marks])#adds the student 
    print("Student Added!")

while True:
    print("\n--- TEACHER'S RANKBOARD ---")
    print("1. Show all students")#prints the name and marks of the student
    print("2. Add new student")#to add a new student marks
    print("3. Change marks")#to change the marks if you entered wrong
    print("4. Show Average")#shows average of the student
    print("5. Show Rank 1 Student")#shows the topper student
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_all()
    elif choice == "2":
        add_student()
    elif choice == "3":
        change_mark()
    elif choice == "4":
        show_average()
    elif choice == "5":
        show_rank1()
    elif choice == "6":
        print("Bye! Keep learning.")
        break
    else:
        print("Wrong choice, try again")

  print("Thank you for choosing Teacher's RankBoard")
