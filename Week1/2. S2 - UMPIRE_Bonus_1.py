# Bismillahir Rahmanir Rahim
# Session 2 - UMPIRE Bonus 1

# Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

# Examples: 
# Input: laboratory, rat
# Output: true

# Input: cat, meow
# Output: false



string1 = input("Please enter the super string: ")
string2 = input("Please enter the sub string: ")

if (string1.find(string2) == -1):
    print("False")
else:
    print("True")