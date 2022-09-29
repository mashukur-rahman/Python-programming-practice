#Write the python programs, which prints the following sequences of values in loops
# 18, -27, 36, -45, 54, -63
count=18
list1=[]
while count<=63:
    list1.append(count)
    count=count+9
for i in range(len(list1)):
    if i%2!=0:
        list1[i]=list1[i]*-1
print(list1)


    
