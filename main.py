print("Welcome to my Tip Calculator, anon!")
#determine bill amount to be paid
total_bill = float(input("What is the total $ bill?\n"))
#determine prefered tip percentage
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
#determine number of persons splitting the bill
splitter_number = int(input("How many people are splitting the bill?\n"))
#calculate the tip amount, round each calculation to 2dp
tip_amount = round((tip_percent / 100), 2)
#calculate the bill to be paid by each person
split_share = round(total_bill/splitter_number, 2)
per_person = round((split_share * tip_amount + split_share), 2)
print(f"Each person should pay: ${per_person}")