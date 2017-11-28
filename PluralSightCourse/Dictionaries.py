student = {
    "name" : "Mark",
    "student_id" : 1234,
    "feedback" : None
}

all_students = [
    {"name":"Marko","student_id":"12345","feedback":None},
    {"name":"Aefs","student_id":"12345","feedback":None},
    {"name":"Alex","student_id":"12345","feedback":None},
]


try:
    print(student["name"])
    print(all_students[0]["name"])
    print(student["buttname"])
except KeyError:
    print("Key not found")