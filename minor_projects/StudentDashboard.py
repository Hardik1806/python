n=int(input("please enter the number of students: "))
student_name=[]# creating empty lists for all inputs
marks_maths=[]
marks_science=[]
marks_english=[]
student_avg=[]
for i in range(n):
    a=input("please enter the name of the student")# using for loop fot taking input of marks and names
    b=int(input("please enter marks scored in maths"))
    c=int(input("please enter the marks scored in science"))
    d=int(input("please enter the marks scored in english"))
    student_name.append(a)
    marks_maths.append(b)#storing the data in lists
    marks_science.append(c)
    marks_english.append(d)
avg=0
def calc_avg(maths,science,english):#function to calculate the average marks
    avg=(maths+science+english)/3

    return avg

for i in range(0,n):
    student_avg.append(calc_avg(marks_maths[i],marks_science[i],marks_english[i]))#appending the averages into the lists

student_grade=[]
for i in range(n):
    if student_avg[i]>=90:
        student_grade.append("A")# calculating the grade and storing it in the list
    elif student_avg[i]>=75 and student_avg[i]<90:
        student_grade.append("B")
    elif student_avg[i]>=60 and student_avg[i]<75:
        student_grade.append("C")
    elif student_avg[i]>=45 and student_avg[i]<60:
        student_grade.append("D")
    else:
        student_grade.append("F")

print("Student-Dashboard:")#printing the output
for i in range(n):
    print(f"Name: {student_name[i]}-> Maths:{marks_maths[i]}, Science:{marks_science[i]}, English:{marks_english}| Avg:{student_avg[i]}| Grade: {student_grade[i]} ")











