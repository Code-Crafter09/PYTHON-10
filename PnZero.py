#Program to check if a number is positive, negative or zero.

num = int(input("Enter a number: "))

if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print("It is Zero!")
else:
    print(num, "is a negative number.")