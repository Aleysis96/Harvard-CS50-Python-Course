import re

name = input("Your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


# := "walrus operator" in if conditions. Allows to assing a value and ask a boolean question
