#Write the Python code of a program that reads two numbers from the user, and prints their sum, product, and difference.
x=int(input('Enter the first number: '))
y=int(input('Enter the second number: '))
sum=x+y
product=x*y
if x>y or x==y:
    difference=x-y
else:
    difference=y-x
print(sum)
print(product)
print(difference)