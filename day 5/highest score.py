student_score= input("Input student scores").split()
for n in range(0, len(student_score)):
    student_score [n]=int(student_score[n])
print (student_score)

maximum=student_score[0]
for current in student_score:
    if current>maximum:
        maximum=current
print (maximum)
