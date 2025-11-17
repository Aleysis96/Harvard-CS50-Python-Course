import csv

name = input("Name? ")
home = input("home? ")

with open("students_write.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
