students = []


def read_file():
    try:
        f = open("Students.txt", "r")
        for student in read_students(f):
            students.append(student)
            f.close()
    except Exception:
        print("File not found")


def read_students(f):
    for f in f.readlines():
        yield f

read_file()
print(students)