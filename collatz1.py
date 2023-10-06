# Author : Michael Allen
# First Assignment for Fundamental Data Analysis

#import the maths module
import math

# create number variable and set it equal to 10000
number = 10000

# create a while loop
# loop keeps going while the number is greater than 0
while number > 0:
    if (number % 2) == 0: #if the number is divided by 2 with remainder equal to zero
        print (str(int(number)), end=' ') #print even number
        number = number/2 # Divide by 2 and update the variable       
         
    elif (number % 2) != 0: # else if the number is divided 2 with remainder not equal to zero
        print (str(int(number)), end=' ') #print odd number
        number = (number * 3) + 1 # Multiply by 3 and update the variable

#Research
#https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
#https://stackoverflow.com/questions/33905032/how-to-print-on-the-same-line-in-python