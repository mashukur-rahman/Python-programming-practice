# Write a Python code that will read 5 numbers from the user. 
# Your program should print the first number, the sum of the first 2 numbers, the sum of the first 3 numbers
# and so on up to the sum of 5 numbers.
sum=0
for i in range(5):
    n=int(input('Enter the number: '))
    if sum==0:
        print(n)
        sum=sum+n
    else:
        sum=sum+n
        print(sum)