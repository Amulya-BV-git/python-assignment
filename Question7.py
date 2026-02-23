def celsius_to_fahrenheit(c):
    return(c*9/5)+32
def fahrenheit_to_celsius(f):
    return(f-32)*5/9
def celsius_to_kelvin(c):
    return c+273.15
def kelvin_to_celsius(k):
    return k-273.15
while True:
    print("\n===== TEMPERATURE CONVERTER=====")
    print("1. celsius to fahrenheit")
    print("2. fahrenheit to celsius")
    print("3. celsius to kelvin")
    print("4. kelvin to celsius")
    print("5. exit")
    choice = input("enter your choice (1-5):")
    if choice == "5":
        print ("exiting program. thank you!")
        break
    try:
        temperature = float(input("enter the temperature value :"))
        if choice =="1":
            result =celsius_to_fahrenheit(temperature)
            print(f"{temperature}degree celsius = {result:.2f}degree fahrenheit")
        elif choice =="2":
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}degree fahrenheit={result:.2f}degree celsius")
        elif choice =="3":
            result = celsius_to_kelvin(temperature)
            print(f"{temperature}degree celsius=:{result:.2f}K")
        elif choice =="4":
            result = kelvin_to_celsius(temperature)
            print(f"{temperature }K={result:.2f}degree celsius")
        else:
            print("Invalid select between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter a numeric temperature.")