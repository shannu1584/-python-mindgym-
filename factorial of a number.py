

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of a",n,"is",fact)
n=int(input())
factorial(n)