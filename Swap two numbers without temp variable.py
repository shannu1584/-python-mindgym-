def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
a,b=swap(a,b)
print("swap of two numbers is:")
print("a:",a)
print("b:",b)