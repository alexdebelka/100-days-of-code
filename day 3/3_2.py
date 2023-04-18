def main():
    weight=float(input("What is yout weight?\n"))
    height=float(input("What is your height?\n"))
    return weight, height
def calculaate_bmi(weight, height):
    bmi= weight/(height*height) *10000
    return bmi
x,y= main()
z= calculaate_bmi(x,y)
# calculaate_bmi(weight, height)
if z<=18.5:
    print("You are underweight")
elif 18.5<z<=25:
    print("You are in normal range")
elif 25<z<=30:
    print("You are overweight")
elif 30<z:
    print("You are obise")
else:
    print("Unrecognized data")
print("Your bmi is: ", z)