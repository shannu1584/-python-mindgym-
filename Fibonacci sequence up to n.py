

def fibnocci(n):
    a=0
    b=1
    for _ in range(n):
        if a>n:
            break
        print(a,end=",")
        a,b=b,a+b
        
n=int(input())
fibnocci(n)