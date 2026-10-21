input("XOR with 0 keeps the number, Press Enter")
print(" 5 ^ 5 =", 5 ^ 5)
print(" 9 ^ 9 =", 9 ^ 9)




input("XOR with itsellf gives 0. Press Enter")
print(" 5 ^ 5 =", 5 ^ 5)
print(" 9 ^ 9 =", 9 ^ 9)

n = int(input("Enter a numebr (try 6 or 11):"))
guess = input("What is 3 ^ " + str(n) + " ^ 3?")
input("XOR cancels - 3 appears twice so it dissapers.Press Enter")
print(" 3 ^", n , "^3 =", 3 ^ n ^ 3, "your guess:", guess)





input("XOR all numbers - pairs cancel, the odd oone stays. Press Enter")
print(" lis: [2,3,4,3,2] ")
print("odd-occuring:", 2^3^4^3^2)

n = int(input("Enter a number (try 7 or 11):"))
nums = [3, n, 5, 3, 5]
guess - input("Which number in" + str(nums) + "appears once?")
result  = 0
for x in nums:
    result ^= x
input("XOR cancel pairs - the odd one survives. Press Enter")
print("list:", nums, " odd-occuring:", result, " your guess:", guess)    





input("XOR all- pairs cancel, two odd occuring ones reamin. Press Enter")
print(" [1,4,3,3] XOR of all:", 1^4^3^3, " binary:", bin(1^4^3^3)[2:])
print(" split bit 1 -> group A (bit 0 ON): 1 group B(bit 0 off): 4")

n - int(input("Enter a number (try  6 or 9): "))
guess = input("Is bit 0 of " + str(n) + "ON? (yes/no): ")
input("Check the split bit. Press Enter")
if n & 1:
    print(" ", n, " binary: ", bin(n)[2:], "bit 0 ON - GROUPA your guess: ", guess)
else:
    print(" ", n, " binary: ", bin(n)[2:], "bit 0 OFF - GROUPB your guess: ", guess)
