print("Student Report Generator")

name = input("Enter Name: ")
reg_no = input("Enter Register Number: ")

mark1 = int(input("Enter marks for social: "))
mark2 = int(input("Enter marks for Evs: "))
mark3 = int(input("Enter marks for Maths: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 90:
    grade = "A+ (Outstanding)"
elif average >= 80:
    grade = "A (Excellent)"
elif average >= 70:
    grade = "B+ (Very Good)"
elif average >= 60:
    grade = "B (Good)"
elif average >= 50:
    grade = "C (Pass)"
else:
    grade = "F (Re-Appear)"
print("STUDENT MARK SHEET")
print(f"Name      : {name}")
print(f"Reg No    : {reg_no}")
print(f"Social    : {mark1}")
print(f"Evs       : {mark2}")
print(f"Maths     : {mark3}")
print(f"Total     : {total} / 300")
print(f"Average   : {round(average, 2)}")
print(f"Grade     : {grade}")
