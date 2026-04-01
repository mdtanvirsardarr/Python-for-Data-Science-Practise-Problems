"""
Fibonacci: A number series where each new number is found by adding the previous two numbers.
Example: 0, 1, 1, 2, 3, 5, 8

Factorial: The product of a number and all positive numbers below it down to 1.
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

Prime number: A number greater than 1 that is divisible only by 1 and itself.
Example: 2, 3, 5, 7

Palindrome: A word, string, or number that reads the same forward and backward.
Example: madam, 121

Armstrong number: A number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits.
Example: 153 = 1³ + 5³ + 3³

Perfect number: it is a positive number that is equal to the sum of its proper factors, excluding the number itself.

Example:
6 is a perfect number because its factors are 1, 2, 3
and 1 + 2 + 3 = 6

A strong number is a number whose value is equal to the sum of the factorials of its digits.

Example:
145 is a strong number because:

1! + 4! + 5! = 1 + 24 + 120 = 145

Harshad number: it is a number that is divisible by the sum of its digits.

Example: 18 is a Harshad number because:

1 + 8 = 9
18 ÷ 9 = 2

Happy number: it is a number that finally becomes 1 when you repeatedly add the squares of its digits.

Example for 19:

1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1

"""

# 1. Check a number is positive, negative or zero
def pos_neg_zero(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


num = int(input("Enter the number to find out positive, negative or zero: "))
print(pos_neg_zero(num))


# 2. Check a number is even or odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number to check  if even or odd: "))
print(even_odd(num))

#3. Factorial of a number
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

num = int(input("Enter any number to find factorial:"))
print(factorial(num))
    
#4. Fibonacci series up to n terms
def fibonacci(n):
    fib_series = []          # Create an empty list to store Fibonacci numbers
    a, b = 0, 1              # Initialize the first two Fibonacci values
    for _ in range(n):       # Repeat the process n times
        fib_series.append(a) # Add the current value of a to the list
        a, b = b, a + b      # Update a and b to the next two Fibonacci values
    return fib_series        # Return the complete Fibonacci series

num = int(input("Enter the number for fibonacci series: "))
print(fibonacci(num))

#5. Check if a number is prime or not
def is_prime(num):
    if num <= 1:
        return False          # Numbers less than or equal to 1 are not prime
    elif num == 2:
        return True           # 2 is the only even prime number
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False  # If divisible by any number, it is not prime
        return True           # If no divisor is found, it is prime

num = int(input("Enter a number to check if it is prime or not: "))
print(is_prime(num))
    
#6. Check if a number if a palindrome or not
def is_palindrome(n):
    original =str(n)
    reversed_num =original[::-1] # Reverse the string representation of the number
    return original ==reversed_num #check if the original and reversed strings are the same

num = int(input("Enter a number to check if it is palindrome or not: "))
print(is_palindrome(num))

#7. Check if a number is an Armstrong number or not
def is_armstrong(n):
    num_str = str(n)  # Convert the number into a string so each digit can be read one by one
    num_digits = len(num_str)  # Count how many digits are in the number
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)  # Add each digit raised to the power of total digits
    return armstrong_sum == n  # Return True if the sum equals the original number

num = int(input("Enter a number to check if it is Armstrong number or not: "))
print(is_armstrong(num))

#8. Check if a number if a perfect number or not
def is_perfect(n):
    if n <= 1:
        return False  # Perfect numbers are greater than 1

    total = 0  # Store the sum of factors

    for i in range(1, n):
        if n % i == 0:
            total = total + i  # Add the factor to total

    if total == n:
        return True  # The number is perfect
    else:
        return False  # The number is not perfect

num = int(input("Enter a number to check if it is perfect or not: "))  # Take input from the user
print(is_perfect(num))  # Print True or False

#9. Check if a number is a strong number or not
def is_strong(n):
    num_str = str(n) #Convert the number into a string to access each digit
    strong_sum = sum(factorial(int(digit)) for digit in num_str) #Calculate the sum of factorials of the digits
    return strong_sum == n 

num = int(input("Enter a number to check if it is strong number or not:"))
print(is_strong(num))

#10. Check if a number is a perfect square or not
def is_perfect_square(n):
    if n < 0:
        return Flase #perfectsquare can not be negative
    root =int(n**0.5) #Calculate the integer square root of the number
    return root * root ==n #Check if the square of the root equals the original number

num = int(input("Enter a number to check if it is perfect square or not:"))
print(is_perfect_square(num))

#11. Check if a number is a perfect cube or not
def is_perfect_cube(n):
    if n < 0:
        return False  # Perfect cubes cannot be negative
    root = int(n ** (1/3))  # Calculate the integer cube root of the number
    return root ** 3 == n  # Check if the cube of the root equals the original number

num = int(input("Enter a number to check if it is perfect cube or not:"))
print(is_perfect_cube(num))

# 12. Check if a number is a Harshad number or not
def is_harshad(n):
    if n <= 0:
        return False  # Harshad numbers are positive integers

    digit_sum = sum(int(digit) for digit in str(n))  # Calculate the sum of the digits
    return n % digit_sum == 0  # Check if the number is divisible by the sum of its digits

n = int(input("Enter a number to check if it is Harshad number or not: "))
print(is_harshad(n))

#13. Check if a number is a happy number or not
def is_happy(n):
    seen = set()  # Store numbers already seen to avoid infinite loop

    while n != 1 and n not in seen:
        seen.add(n)  # Add current number to the set
        n = sum(int(digit) ** 2 for digit in str(n))  # Find sum of squares of digits

    return n == 1  # If n becomes 1, it is a happy number

n = int(input("Enter a number to check if it is a happy number or not: "))
print(is_happy(n))

#14. Swap 2 number without using a temporary variable
def swap(a,b):
    a = a+b # Add the two numbers and store the result in a 
    b = a-b # Subtract the new value of a form the new value of a and store the result in b (which is the original value of a)
    a = a-b # Subtract the new value of b from the new value of a and store the result in a (which is the original value of b)
    return a,b

a= int(input("Enter the first numeber:"))
b= int(input("Enter the second numeber:"))
a,b = swap(a,b)
print("After swapping:")
print("First number:", a)
print("Second number:", b)


#15.Reverse a number
def reverse_number(n):
    reversed_num =0 # Initialize the variable to store the reversed numebr
    while n>0:  #Continue the loop until n becomes 0
        digit = n % 10 #Extract the last digit of n
        reversed_num = reversed_num * 10 + digit # Add the extracted digit to the reversed number and shift the previous digits the left by multiplying by 10
        n = n// 10 #Remove the last digit from n by performing integer division by 10 
        return reversed_num 
a= int(input("Enter the first number:"))
print("Reversed number:", reverse_number(a))
