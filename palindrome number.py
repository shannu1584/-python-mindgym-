def palindrome(n):
    rev=0
    t=n
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print("reverse of a number:",rev)
    if(t==rev):
        print("palindrome")
    else:
        print("Not a palindrome")
n=int(input())
palindrome(n)