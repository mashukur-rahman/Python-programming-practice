# Write the Python code of a program that adds all numbers that are multiples of both 7 and 9 up to 600 (including 600) i.e. 63, 126, 189, 252, ....
# The output of your program should be: 2835
# since 63 + 126 + 189 + 252 + 315 + 378 + 441 + 504 + 567 = 2835
count=0
sum=0
while count<=600:
    if count%7==0 and count%9==0:
        sum+=count
    count+=1
print(sum)
