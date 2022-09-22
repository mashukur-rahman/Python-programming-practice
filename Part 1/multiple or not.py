# Write the Python code of a program that reads an integer as input from the user, and 
# prints the integer if it is a multiple of 2 OR 5 and prints "Not a multiple of 2 OR 5" otherwise.

x=int(input('Enter the integer: '))
if x%5==0 or x%2==0:
    print(x)
else:
    print('Not a multiple')
