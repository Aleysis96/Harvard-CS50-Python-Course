students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is from {student['home']}")

#lambda is used when no need to create a def function that is only called one time
