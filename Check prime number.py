n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Not a prime Number")

def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print("Prime")
    else:
        print("Not a prime")
n=int(input())
isprime(n)