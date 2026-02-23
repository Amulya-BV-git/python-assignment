from datetime import datetime
year = int(input("Enter birth year:"))
age = datetime.now().year - year
print("CURRENT AGE:",age)
print("AGE IN MONTHS:", age*12)
print("AGE IN DAYS:", age*365)
print("AGE IN HOURS:", age*24)
print("AGE IN MINUTES:", age*60)
print("YEARS UNTIL AGE 100:",age*100)