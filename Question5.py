total_bill=float(input("Enter total_bill:"))
people=int(input("number of People:"))
tax_percent=float(input("Tax percentage:"))
tip_percent=float(input("Tip_percentage:"))
tax_amt=total_bill*tax_percent/100
after_tax=total_bill+tax_amt
tip_amt=after_tax*tip_percent/100
final_total=after_tax+tip_amt
per_person=final_total/ people
print("Total:",final_total)
print("Per_person:", final_total/people)
print("\n===BILL BREAKDOWN===")
print(f"subtotal:₹{total_bill:.2f}")
print(f"Tax({tax_percent}%):₹{tax_amt:.2f}")
print(f"Tip({tip_percent}%):₹{tip_amt:.2f}")
print(f"Total:₹{final_total:.2f}")
print(f"Per_person:₹{per_person:.2f}")