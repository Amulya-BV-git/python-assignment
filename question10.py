balance = 10000
PIN = 1234
def check_balance():
    print(f"\nCurrent Balannce: ₹{balance:.2f}")
def deposit ():
        global balance
        try:
            amount = float(input("Enter amount to deposit:") )
            if amount > 0:
                balance+=amount
                print(f"₹{amount:.2f}deposited successfully")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid amount entered.")
def withdraw():
    global balance
    try:
        amount=float(input("Enter amount to withdraw:"))
        if amount <=0:
            print("Withdraw amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
            print(f"₹{amount:.2f}withdraw successfully.")
    except ValueError:
        print("Invalid amount enterned.")
print("=======WELCOME TO ATM=======")
try:
    entered_pin= int(input("Enter your PIN:"))
    if entered_pin!=PIN:
        print("Incorrect PIN. Access Denied.")
    else:
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw money")
            print("4. Exit")
            choice=input("Choose an Option(1-4):") 
            if choice=="1":
                check_balance()
            elif choice=="2":
                deposit()
            elif choice =="3":
                withdraw()
            elif choice=="4":
                print("Thank you for using ATM. ")
                break
            else:
                print("Invalid choice. Please select 1-4.") 
except ValueError:
    print("Inavalid PIN format.")             