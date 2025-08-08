def convert(n):
    return f"""
    Binary:{bin(n)}
    Octal:{oct(n)}
    hexadecimal:{hex(n)}"""
num=int(input("Enter number:"))
print(convert(num))