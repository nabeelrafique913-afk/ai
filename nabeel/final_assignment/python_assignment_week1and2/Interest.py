# Calculate Compound Interest 
# Use the formula: 
# CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time 

p=int(input("enter  a principlae "))
r=int(input("enter rate"))
t=int(input("enter a time "))
cl= p*(1+r/100)**t-p
print("your compound inerest is ",cl)
