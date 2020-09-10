on = True
def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a+b)

def subtraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number ."))
    print(a-b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number ."))
    print(a*b)

def divide():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print(a/b)

while on:
    operation = input("Please type *, +, / , - or q")

    if operation == '*':
         multiply()
    elif operation == '+':
       add()
    elif operation == '/':
       divide()
    elif operation == 'q':
        on = False
    else:
       print("That operation is not available. ")
