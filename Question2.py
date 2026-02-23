try:
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    print("Addition:",a+b)
    print("Subraction:",a-b)
    print("Multiplication:",a*b)
    if b !=0:
        print("Division:",a/b)
        print("Modulus:",a%b)
    else:
        print("Division ny zro not allowed")
        print("Ppoer:",a**b)
except:
    print("Invalid input")

