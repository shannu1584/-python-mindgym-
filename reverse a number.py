
def reverse(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print("reverse:",rev)
n=int(input())
reverse(n)