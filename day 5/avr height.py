student_heights= input("Input student heights").split()
for n in range(0, len(student_heights)):
    student_heights [n]=int(student_heights[n])
print (student_heights)

total_h=0
for h in student_heights:
    total_h+= h
print(total_h)

nr_students=0
for students in student_heights:
    nr_students+=1
print(nr_students)

avr= round(total_h/nr_students)
print(avr)