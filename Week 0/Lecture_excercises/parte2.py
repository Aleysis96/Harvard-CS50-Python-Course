# Declare variable for input + remove spaces (if any) & capitalize user´s name
name = input("Hola :) ¿Cómo te llamas? ").strip().title()
# Print variable of input result
print(f"Gusto en conocerte, {name} :)")
# Declares variables for age and remove spaces if any
# 'f' function is a modern way to concatenate all variables into one line
edad = input(f"Dime, {name}, ¿qué edad tienes? ").strip()
# Print variable of input result
# 'f' function is a modern way to concatenate all variables into one line
print(f"¡Wow! tienes {edad} años, ya estás grande {name} :D")
