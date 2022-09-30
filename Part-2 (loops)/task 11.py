# Write a Python program which takes a number and prints the digits from the unit place, 
# then the tenth, then hundredth, etc. (Right to Left)
# Consider the input number to be an INTEGER. 
# You are not allowed to use String indexing for solving this task]
# Example: If the user gives 32768, then print 8, 6, 7, 2, 3
n=int(input('Enter the number: '))
while n!=0:
    number=n%10
    n=n//10
    print(number,end=', ')

