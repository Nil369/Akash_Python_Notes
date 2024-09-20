score = int(input("Enter your score: "))

if score >=101:
    print("Invalid score!! Please Try again")
    exit()

if score >= 90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")