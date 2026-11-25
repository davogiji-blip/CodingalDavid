print("My Countdown")

def countdown(number):
    # Base Case
    if number == 0:
        print("Time is up!")
        return

    print(number)
    countdown(number - 1)

print("Countdown from 5:")
countdown(5)


def build_and_unwind(level):
    # Base Cas
    if level == 0:
        print("Base case reached. Now unwinding begins.")
        return

    print("Building level:", level)
    build_and_unwind(level - 1)
    print("Unwinding level:", level)


print("Build and Unwind Demo:")
build_and_unwind(3)


def count_up(number):
    # Base Case
    if number > 10:
        return

    print(number)
    count_up(number + 1)

print("Counting from 1 to 10:")
count_up(1)

def factorial(number):
    # Base Case
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial Result:")
print("3! =", factorial(3))

def unsafe_countdown(number):
    print(number)
    # Missing base case - this can cause stack overflow
    # unsafe_countdown(number - 1)


print("Stack Overflow Note:")
print("A recursive function must have a base case to stop safely.")
print("The unsafe_countdown function is written but not called.")
print("================================")
