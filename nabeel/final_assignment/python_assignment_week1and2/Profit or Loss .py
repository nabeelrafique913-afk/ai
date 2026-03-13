# Question 8: 
# Calculate Profit or Loss 
# Input cost price and selling price. Display either: 
# Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss 

# Question 8:
# Calculate Profit or Loss

cost = int(input("Enter cost price: "))
selling = int(input("Enter selling price: "))

if selling > cost:
    profit = selling - cost
    print("Profit =", profit)
elif cost > selling:
    loss = cost - selling
    print("Loss =", loss)
else:
    print("No Profit, No Loss")
 