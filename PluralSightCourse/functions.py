students = []


def get_students_titlecase():
    student_title_case = []
    for student in students:
        student_title_case.append(student["name"].title())
    return student_title_case


def print_student_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)


def save_file(student):
        try:
            f = open("Students.txt","a")
            f.write(student + "\n")
            f.close()
        except Exception:
            print("File could not be opened")

def read_file():
    try:
        f = open("Students.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("File could not be opened")


def add_student(name, student_id = 332):
    student = {"name": name, "student_id":student_id}
    students.append(student)

student_list = get_students_titlecase()

while True:
    want_to_add = input("Do you want to add a student? Y/N ")
    if want_to_add == "Y":
        student_name = input("Enter student name: ")
        student_id = input("Enter student id: ")
        #save_file(student_name)
        add_student(student_name, student_id)
    elif want_to_add == "N":
        #read_file()
        print_student_titlecase()
    elif want_to_add != "N" or "Y":
        print("Incorrect Input")