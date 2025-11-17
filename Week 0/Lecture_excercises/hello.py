# We defined a function
def prueba():
    # Declare variable for input
    print("Holaaaaaa :) ")
    name = input("Como te llamas? ")
    # Remove whitespace from input (if any) and capitalize user's name
    name = name.strip().title()
    # Print variable of input result in a simple way
    print("Gusto en conocerte ", name, ":)")
    return name

# We defined other function that can work with the value from the first function
def age(name):
    edad = int(input("Tu edad "))
    if edad >= 18:
        print("Bienvenid@")
        input("Dime, " + name +  ", ¿Como puedo ayudarte hoy? ")
        return True
    else:
        print("Lo siento, no puedo ayudarte", ":(")
        return False


while True:
    nombre = prueba() # if the condition is false, runs the first function and starts again
    if age(nombre): # if the conditon is true it stops
        break

