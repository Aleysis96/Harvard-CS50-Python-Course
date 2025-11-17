names = []

with open("names.txt") as file:
    for line in sorted(file):
        names.append(line.rstrip()) # removes blank space within the list

for name in sorted(names):
    print(f"hello, {name}")

#sorted(names, reverse=True): -- for sorting in descending
