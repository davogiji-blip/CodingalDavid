def sum_down(n):
    if n == 0:
        return 0
    return n + sum_down(n - 1)

input("Recursion - a function calls itself until a base case stops it. Press Enter")
print(" sum_down(3) = 3 + 2 + 1 + 0 = ", sum_down(3))
print(" sum_down(4) = 4 + 3 + 2 + 1 + 0 = ", sum_down(4))

n = int(input("Enter a number (try 5 or 6): "))
guess = input("What is sum_down(" + str(n) + ")? ")
input("sum_down adds n to sum_down(n-1) until n is 0. Press Enter")
print(" sum_down(" + str(n) + ") = ", sum_down(n), " your guess:", guess)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

input("Factorial - n! = n * (n-1)* ..... *1 base case: 0! = 1. Press Enter")
print(" 4! =", factorial(4),  " = 4 * 3 * 2 * 1  ")
print(" 5! =", factorial(5),  " = 5 * 4 * 3 * 2 * 1  ")

n = int(input("Enter a number (try 5 or 6): "))
guess = input("What is " + str(n) + "!? ")
input("n! = n * factorial(n-1) base case: 0! = 1. Press Enter")
print(" " + str(n) + "! = ", factorial(n), " your guess:", guess)

def sum_down(n):
    if n == 0:
        return 0
    return n + sum_down(n - 1)

input("Stack overflow - each calls adds a frame to the stack limit is 1000. Press Enter")
print(" sum_down(3) =" sum_down(3), " uses 3 frames")
print(" sum_down(5) =" sum_down(5) , " uses 5 frames")

n = int(input("Enter a number (try 6 or 9): "))
input("sum_down(n) = n + (n -1) + ... + 1 uses n frames. Press Enter) until n is 0. Press Enter")
print(" sum_down(" + str(n) + ") = ", sum_down(n), " frames used:", n)
