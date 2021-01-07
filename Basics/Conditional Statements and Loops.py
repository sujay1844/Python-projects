print("Hello! Welcome to Pasadena")
Array = ["Sheldon", "Leonard", "Penny", "Rajesh"]
for i in range(0,len(Array)):
    x = Array[i]
    if x == "Sheldon":
        print("Hi Sheldon")
    elif x == "Leonard":
        print("Hi Leonard")
    elif x == "Penny":
        print("Hi Penny")
    else:
        print("I'm sorry. Who are you,", x,"\b?")
