# Write a Python code that will calculate the value of y if the expression of y is as follows (n is the input):
# 𝑦=1^2−2^2+3^2−4^2+5^2.........+𝑛^2
n=int(input('Enter a number: '))
y=0
for i in range(1,n+1):
    if i%2!=0:
        y=y+(i**2)
    elif i%2==0:
        y=y-(i**2)
print(y)