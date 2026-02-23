def print_table(number,limit):
    print (f"\nmultiplication Table for {number}(up to{limit})")
    print("-"*40)
    for i in range (1,limit+1):
        print(f"{number}x{i}={number*i}")
try:
    num=int(input("Enter a number:"))
    limit=int(input ("Enter range limit:"))
    if limit<=0:
        print("Range must be geater than 0.")
    else:
        print_table(num,limit) 
except ValueError:
    print("Inavlid input! Please enter integers only.")             
