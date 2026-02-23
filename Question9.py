def calculate_ticket_price(age):
    """return base ticket price based on age."""
    if age<5:
        return 0
    elif age <= 12:
        return 150
    elif age <=59:
        return 250
    else:
        return 180
def day_discount(total_amount, day):
        """apply discount based on day"""
        day=day.lower()
        if day =="Wednesday":
            print("Midweek offer applied (20%  discount)")
            return total_amount*0.20
        elif day == "Monday":
            print("Monday offer applied (10% discount)")
            return total_amount*0.10
        else:
            return 0
try:
            age = int (input("Enter your age."))
            tickets=int(input("Emter number of tickets:"))
            day=input("enter day of booking:")
            base_price=calculate_ticket_price(age)
            subtotal=base_price*tickets
            discount=day_discount(subtotal,day)
            final_amount=subtotal-discount
            print("\n=====TICKET BILL======")
            print(f"Base ticket price:₹{base_price:.2f}")
            print(f"Number of tickets:{tickets}")
            print(f"Subtotal: ₹{subtotal:.2f}")
            print(f"Discount:₹{discount:.2f}")
            print(f"Final amount:₹{final_amount:.2f}")
except ValueError:
            print("Invalid input! Please enter correct numeric values.")