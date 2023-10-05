# Making a Tip calculator for the Udemy Course
# the cal with have the input for the original bill ammount
# options for a 10% 12% or 15% tip
# also there will be a prompt for the number of people at the table

print("Welcome to the tip Calculator!")
#user inputs
bill = float(input("What was the ammount of the bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many ways is the bill being split? "))

#calculations
tip_as_percent = tip/100
total_tip_ammount = bill * tip_as_percent
total_bill = bill +total_tip_ammount
tip_per_person = round(total_tip_ammount/ people,2)
bill_per_person = round(total_bill / people, 2)
bill_per_person = "{:.2f}".format(bill_per_person)

#results
print(f"Each person should pay{bill_per_person},which includes a {tip_per_person} per person")

