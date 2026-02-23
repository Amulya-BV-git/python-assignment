def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True
try:
    num = int(input("Enter a number:"))
    if is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a PRIME number ")
except ValueError:
    print("Invalid input! Please enter an integer.")
try:
    start = int(input("\nEnter start range:"))
    end = int(input("Enter end range:"))
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(str(number))
    print("Prime numbers: ","," .join(primes) )       
except ValueError:
    print("Invalid range input!")

