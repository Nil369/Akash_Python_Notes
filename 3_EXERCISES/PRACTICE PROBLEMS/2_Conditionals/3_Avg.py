# WRITE A PROGRAM in Python to enter marks in 5 subjects out of 100 Calculate the average
# marks and provide the grades accordingly

subject1 = float(input("Enter your marks in subject 1: "))
subject2 = float(input("Enter your marks in subject 2: "))
subject3 = float(input("Enter your marks in subject 3: "))
subject4 = float(input("Enter your marks in subject 4: "))
subject5 = float(input("Enter your marks in subject 5: "))


total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = (total_marks / 500) * 100

if average_marks <= 100 and average_marks >= 90:
    grade = "Ex"
elif average_marks < 90 and average_marks >= 80:
    grade = "A"
elif average_marks < 80 and average_marks >= 70:
    grade = "B"
elif average_marks < 70 and average_marks >= 60:
    grade = "C"
elif average_marks < 60 and average_marks >= 50:
    grade = "D"
elif average_marks < 50:
    grade = "F"

print(f"Your Percentage is: {round(average_marks, 2)}%\nYour grade is: {grade}")



# sol 2 - using list:

"""
marks =[]
for i in range(1,6):
    sub_marks = float(input(f"Enter your marks in subject {i}: "))
    marks.append(sub_marks)

total_marks = sum(marks)
average_marks = ((total_marks/500)*100)

if(average_marks<=100 and average_marks>=90):
    grade = "Ex"
elif(average_marks<90 and average_marks>=80):
    grade = "A"
elif(average_marks<80 and average_marks>=70):
    grade = "B"
elif(average_marks<70 and average_marks>=60):
    grade = "C"
elif(average_marks<60 and average_marks>=50):
    grade = "D"
elif(average_marks<50):
    grade = "F"

print(f"Your Percentage is : {round(average_marks, 2)}%\nYour grade is: {grade}")

"""