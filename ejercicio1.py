import sys
import sys

input = sys.stdin.readline

#-----------------------Functions-----------------------


# Takes user input and returns the input as an integer.
def inp() :
    return(int(input()))

# Converts space-separated user input into a list of integers.
# Return a list of integers parsed from the user input.
def inlt() :
    return(list(map(int,input().split())))

# Takes user input and returns a list containing all characters of the input string except the last one.
def insr():
    s = input()
    return(list(s[:len(s) - 1]))

# Takes user input, splits it, and returns a map object with integer values.
def invr():
    return(map(int,input().split()))

#---------------------------------------------------------

words = inp()

for i in range(words):
    word = insr()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(''.join(word))
