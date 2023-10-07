# Author : Michael Allen
# First Assignment for Fundamental Data Analysis

def f(x):
        if (x % 2) == 0: #if the number is divided by 2 with remainder equal to zero 
            return (x // 2)      
         
        else: # else if the number is divided 2 with remainder not equal to zero
            return (x * 3) + 1
        
def collatz(x):
     print(f'Testing Collatz with initial value {x}')
     while x != 1:
          x=f(x)
          print(x)

collatz(5)
        