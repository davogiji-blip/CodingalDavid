for number in range(5,50):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
          
    if isPrime:
        print(number, "is a prime number")
   
