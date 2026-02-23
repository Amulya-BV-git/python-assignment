marks=[]
print("enter marks for 5 subjects(out of 100 each):")
for i in range (1, 6):
    mark=float(input(f"subject{i}:"))
    marks.append(mark)
total=sum(marks)
percentage=total/5
if 90 <=percentage <=100:
    grade="A+(outstanding)"
elif 80 <=percentage <90:
    grade="A(excellent)"
elif 70 <= percentage <80:
    grade="B(good)"
elif 60 <= percentage <70:
    grade="C(average)"
elif 50 <= percentage <60:
     grade="D(pass)"
else:
    grade = "F(fail)"
if all(mark >= 40 for mark in marks):
        result="pass"
else:
        result="fail"
print("\n=== RESULT SUMMARY ====")
for i in range(5):
        print(f"subject {i+1}:{marks[i]}")
        print(f"\n total marks(out of 500):{total}")
print(f"percentage:{percentage: .2f}%")
print(f"grade:{grade}")
print(f"final Result:{result}")