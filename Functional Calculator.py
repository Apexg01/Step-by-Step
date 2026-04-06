print("Welcome to Calculator")

a = int(input("Enter number \"A\": "))
b = int(input("Enter number \"B\": "))

ab = input("PLEASE NOTE: STATE THE OPERATION EXACTLYAS MENTIONED IN THE BELOW COLUMN \n  Enter the operation you want to perform (+, -, x, /, or add, subtract, multiply, divide): ")

if ab == "+" or ab == "add":
    print(a + b)
elif ab == "-" or ab == "subtract":
    print (a-b)
elif ab == "x" or ab == "multiply":
    print(a*b)
elif ab == "/" or ab == "divide":
    print(a/b)
