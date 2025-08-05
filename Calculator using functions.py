def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return " Cannot divide by zero"
print("Caluclate the operations are +,-,*,/")
operator=input("Enter Operator:")
a=float(input("Enter 1st number:"))
b=float(input("Enter second number:"))
if operator=='+':
    print("Addition:",add(a,b))
elif operator=='-':
    print("Subraction:",sub(a,b))
elif operator=='*':
    print("Multipication:",multiply(a,b))
elif operator=='/':
    print("Division:",divide(a,b))
else:
    print("Invalid Operator")