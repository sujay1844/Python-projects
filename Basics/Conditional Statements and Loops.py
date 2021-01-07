# Since I know Java, I know about conditional statements and loops
# So I just learned the syntax of them in Python

print("Hello! Welcome to Pasadena")

# First, we create an array of names
Array = ["Sheldon", "Leonard", "Penny", "Rajesh"]

# Then, we check which name is being passed and print the corresponding statement
for i in range(0,len(Array)):
    x = Array[i]
    if x == "Sheldon":
        print("Hi geek")
    elif x == "Leonard":
        print("Hey shortie")
    elif x == "Penny":
        print("Yo broke girl")
    else:
        print("I'm sorry. Who are you,", x,"\b?")
