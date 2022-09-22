# Write the Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5
# but not both. If the number is a multiple of 2 and 5 both, then print "Multiple of 2 and 5 both". For all other
# numbers, the program prints "Not a multiple we want".
x=int(input("Enter the number: "))
if x%2==0 and x%5!=0:
    print(x)
elif x%2!=0 and x%5==0:
    print(x)
elif x%2==0 and x%5==0:
    print('Multiple of both 2 and 5')
else:
    print('Not a multiple we want')
