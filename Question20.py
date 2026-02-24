def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *=1
    return result
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a+b 
    return a
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = int(str(n)[::-1])
    return sign * reversed_num
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits) 
    return total == n
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
def lcm (a, b):
    return abs(a*b) // gcd(a, b) 
def is_perfect_number(n):
    if n <= 0:
         return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n 
def math_menu():
    while True:
        print("\n===== NUMBER SYSTEM MENU=====")
        print("1. Factirial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")                
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect NUmber")
        print("0. Exit")
        choice = input("Enter your Choice:")
        if choice == "1":
            n = int(input("enter number:"))
            print("Factorial:", factorial(n))
        elif choice == "2":
            n= int(input("enter number:"))
            print("Prime :", is_prime(n))
        elif choice == "3":
            n= int(input("enter position:"))
            print("Fibonacci:", fibonacci(n))    
        elif choice == "4":
            n= int(input("enter number:"))
            print("Sum of digits:", sum_of_digits(n)) 
        elif choice == "5":
            n= int(input("enter number:"))
            print("reversed number:", reverse_number(n))
        elif choice == "6":
            n= int(input("enter number:"))
            print("Is Armstrong:" ,is_armstrong(n)) 
        elif choice == "7":
            a= int(input("enter first number:"))
            b= int(input("enter second number:"))
            print("GCD:", gcd(a, b))
        elif choice == "8":
            a= int(input("enter first number:"))
            b= int(input("enter second number:"))
            print("LCM:", lcm(a, b))
        elif choice == "9":
            n= int(input("enter number:"))
            print("Is Perfect number  :", is_perfect_number(n)) 
        elif choice == "0":
            print("Exiting program....")
            break
        else:
            print("Inavalid choice! Please try again.")
math_menu()