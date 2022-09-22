# Write the Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds. 
# The number of seconds is taken as input from the user.
x=float(input('Enter seconds: '))
hours=int(x/3600)
minutes=int((x%3600)/60)
seconds=int((x%3600)%60)
print(hours)
print(minutes)
print(seconds)



