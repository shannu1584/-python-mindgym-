def sumofdigit(n):
    sum=0
    t=n
    while n!=0:
        digit=n%10
        sum+=digit
        n=n//10
    print("sum of digit",t,"is:",sum)
n=int(input())
sumofdigit(n)
    