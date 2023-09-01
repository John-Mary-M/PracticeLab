'''cs50p 23/08/2023 Lists and dictionaries'''
# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# print(students[0])
# for student in students:
#     print(student)
# for student in range(len(students)):
#     print(student + 1, students[student])

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Dreco": "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep=": ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "Patronous": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "Patronous": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "Patronous": "Jack Russell terrir"},
    {"name": "Dreco", "house": "Slytherin", "Patronous": None}
    ]
for student in students:
    print(
        student["name"],
        student["house"],
        student["Patronous"],
        sep=": "
    )
    