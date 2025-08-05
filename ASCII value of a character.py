def ascii(a):
    if len(a)==1:
        return f"ASCII value of a character is: {ord(a)}"
    else:
        return "Please enter single character only"
a=input("Enter Character:")
print(ascii(a))