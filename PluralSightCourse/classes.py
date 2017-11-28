students = []


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalise(self):
        return self.name.capitalize()

mark = Student("mark")
print(mark.get_name_capitalise())

