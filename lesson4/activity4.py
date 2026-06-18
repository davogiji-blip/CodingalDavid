n=int(input("Enter a number:"))
if n>1:
    for i in range(2,t(num**0.5)+1):
        if n%i==0:
            print("Not a prime")
        else:
            print("prime")
else:
    print("not prime")