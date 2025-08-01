def armstrong(n):
    t=n
    sum=0
    order=len(str(n))
    while n!=0:
        digit=n%10
        sum+=digit ** order
        n=n//10
    if sum==t:
        print("Armstrong Number")
    else:
        print("Not a Armstrong number")
n=int(input())
armstrong(n)