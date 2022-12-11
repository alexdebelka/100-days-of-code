row_1= ["🟥", "🟥", "🟥"]
row_2= ["🟥", "🟥", "🟥"]
row_3= ["🟥", "🟥", "🟥"]
map=[row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")
nr_x= input("Where do you want to position the x? Give a 2 digit number between 11 and 33 \n")
horizontal= int(nr_x[0])
vertical= int(nr_x[1])
map[vertical-1][horizontal-1]= "X"
print(f"{row_1}\n{row_2}\n{row_3}")