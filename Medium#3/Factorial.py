import math

def cal_factorial(n):
    result = math.factorial(n)
    
    return result
  
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is: {cal_factorial(number)}")
