#star pattern
n=int(input("Enter the number of stars: "))
for i in range(1,n+1):
    for j in range(i):#column
        print("*",end=" ") 
    print()   
    
