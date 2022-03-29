#This is a program that determines whether a number is a prime number

num = int(input("Enter number: "))

def isPrime(num):
    if num == 2 or num == 1 or num % 2 == 0:
        return False
    else:
        return True
if isPrime(num) is True:
    print("{} is a prime number".format(num))
else:
    print("{} is NOT a prime number".format(num))

