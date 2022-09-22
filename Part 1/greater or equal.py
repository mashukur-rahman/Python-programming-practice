# Write the Python code of a program that reads two numbers from the user. 
# The program should then print "First is greater" if the first number is greater
# "Second is greater" if the second number is greater, and "The numbers are equal" otherwise
x=float(input("Enter the first number: "))
y=float(input('Enter the second number: '))
if x>y:
    print('First is greater')
elif x==y:
    print('The numbers are equal')
else:
    print('Second is greater')

