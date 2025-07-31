def count(n):
    count=0
    if n==0:
        count=0
    else:
        while n!=0:
            n=n//10
            count+=1
    print("count of a digit",n,"is",count)
n=int(input())
count(n)