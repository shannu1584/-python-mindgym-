def sumofn(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return f"Sum of first {n} natural numbers is:{sum}"
n=int(input("Enter number:"))
print(sumofn(n))