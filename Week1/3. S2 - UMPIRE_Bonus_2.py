# Bismillahir Rahmanir Rahim
# Session 2 - UMPIRE Bonus 2

# Given a number, return the next smallest prime number

# Examples:
# Input: 3
# Output: 5



import math

# prime check function
def isPrime(nextPrime):
    if(nextPrime % 2 == 0 or nextPrime % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(nextPrime) + 1), 6):
        if(nextPrime % i == 0 or nextPrime % (i + 2) == 0):
            return False

    return True

# next prime function
def nextPrime(possiblePrime):

    prime = possiblePrime
    found = False

    while(not found):
        prime += 1

        if(isPrime(prime) == True):
            found = True

    return prime

# main part
userInput = int(input("Please enter a number: "))
print(nextPrime(userInput))