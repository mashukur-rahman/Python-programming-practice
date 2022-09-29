# Write a Python code of a program that asks the user to enter ten numbers 
# and then display the total and the average of ONLY the odd numbers among those ten numbers.
# [Please do not use list for this task]
count=0
total=0
average=0
for i in range(0,10):
    n=int(input())
    if n%2!=0:
        total+=n
        count=count+1
        average=total/count        
print(total)
print(average)