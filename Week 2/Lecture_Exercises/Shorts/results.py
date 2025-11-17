results = ["Mario", "Luigi"] # list of values

results.append("Princess") # add a new value to the list
results.extend(["Bowser", "Donkey Kong"]) # add more than one value to the list
results.remove("Bowser") # remove a value from a list
results.insert(0, "Bowser") # add a new value to a specific order(rank) within the list
results.reverse() # Change the order(rank) of the list, starting from the last to first now

print(results)
