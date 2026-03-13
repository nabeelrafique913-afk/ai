# Question 17: 
# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes 

m=int(input("enter number of minutes"))
h=m//60
m=m%60
print("hours",h,"miuets",m)
