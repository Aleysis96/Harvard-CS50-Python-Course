import csv

name = input("Name? ")
home = input("home? ")

with open("students_write.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
