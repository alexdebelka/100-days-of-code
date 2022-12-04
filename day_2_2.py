age=int(input("What is your age?\n"))
years_left=90
total_weeks= 90*52
total_days= 90*365
total_months= 90*12
remain_months= total_months - age*12
remain_weeks= total_weeks - age*52
remain_days= total_days - age*365

print(f"You have {remain_months} months, {remain_weeks} weeks, and {remain_days} days left")