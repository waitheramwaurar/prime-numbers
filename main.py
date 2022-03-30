#This is a program that determines whether a number is a prime number
import math

num = int(input("Enter number: "))

def isPrime(num):
    if num == 2:
        return True
    elif num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


if isPrime(num) is True:
    print("{} is a prime number".format(num))
else:
    print("{} is NOT a prime number".format(num))

