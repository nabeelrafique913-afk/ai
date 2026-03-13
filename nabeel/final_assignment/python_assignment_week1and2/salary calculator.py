# Question 10: 
# Salary Calculator 
# Input basic salary. Calculate: 
#  HRA = 20% of basic 
#  DA = 15% of basic 
#  Total Salary = Basic + HRA + DA 
basic=int(input("enter your basic salary"))
hra=0.20*basic
print("20 percent of basic salary is",hra)
da=0.15*basic
print("the 15 percent od basic salary is ",da)
totalsalary=basic+hra+da
print("total salary is ",totalsalary)