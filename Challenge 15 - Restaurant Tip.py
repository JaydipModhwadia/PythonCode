Split=int(input("How many people are splitting?\n"))
Bill=float(input("What is the Total bill?\n"))
Tip=float(input("How much out of 100% would you like to tip (no percent sign in input please)\n"))
TipTotal=float(Bill + (Bill * (Tip/100)))
BillHalf=TipTotal/Split
print("Based on our system, if you were to give a", Tip, "%", "Tip, and you had a bill of", "£", Bill, "And Had", Split, "People Splitting the Bill, Then you would each need to give", BillHalf, "Each")
