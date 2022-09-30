# Write a Python program that takes a number and prints how many digits are in that number.
# [Consider the input number to be an INTEGER.]

# [You are not allowed to use len() function]

# Example: If the user gives 9876, your program should print 4.

n=int(input('Enter the number: '))
count=0
while n!=0:
    n=n//10
    count+=1
print(count)