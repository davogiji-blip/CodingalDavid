n=int(input("Enter a number: "))
digits=0
temp=n
while temp>0:
    digits+=1
    temp=temp//10
temp=n
arm=0
while temp>0:
    digit=temp%10
    arm+=digit**digits
    temp=temp//10
if arm==n:
    print("Armstrong")
else:
    print("Not Armstrong")
