# Write the Python code of a program that displays all the odd numbers between 10 and 50 (inclusive).

# Output: 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49
for i in range(10, 50):
    if i%2!=0:
        print(i,end=' ')