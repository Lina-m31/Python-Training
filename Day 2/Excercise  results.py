#EX1: Write a Python function that takes two integers as input, and then prints the sum, difference, and product of the two numbers.

def calculate(int1: int, int2: int):
    sum=int1 + int2 
    diff=abs(int1-int2) 
    product=int1*int2 
    return (sum , diff ,product)

calculate(3,9)


#Testing Factorial:
import factorial as fact
print (fact.factorial(5))
print (fact.list_factorial([1,2,3,4,5]))


#calculating the prime numbers (the prime function is in module Prime)
import Prime 

print(Prime.is_prime(7))
print(Prime.is_prime(8))

# Testin the math module
import math_utils as MU
a = 10
b = 5
print(f"Addition: {MU.add(a, b)}")        
print(f"Subtraction: {MU.subtract(a, b)}")  
print(f"Multiplication: {MU.multiply(a, b)}")  
print(f"Division: {MU.divide(a, b)}")      
     