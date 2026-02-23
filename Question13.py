def calculate_statistics(numbers):
    total =sum(numbers)
    average =total/len(numbers)
    maximum =max(numbers)
    minimum =min(numbers)
    return total,average,maximum,minimum
try:
    count=int(input("How many numbers do you want to enter?"))
    if count<=0:
        print("Count must be greater than 0.")
    else:
        numbers=[]
        for i in range(1, count + 1):
            num = float (input(f"Enter number{i}:"))
            numbers.append(num)
            total,average,maximum,minimum= calculate_statistics(numbers)
            print("\n===RESULT SUMMARY===")
            print(f"Numbers Entered:{numbers}")
            print(f"Sum:{total:.2f}")
            print(f"Average:{average:.2f}")
            print(f"Maximum Number:{maximum}")
            print(f"Minimum Number:{minimum}")
except ValueError:
    print("Invalid input! Please enter numeric values only.")                