import math
#Coding Exercise 2:
#1. 
x=50
print (x+50, 2*x-10)

#2
#30+*6 => error
print(6**6,6^6, 6+6+6+6+6+6) # 6^6 defaults to 6.__xor__(6) 

#3
print("Hello World", "Hello World : 10")

#4
pv=int(input("Enter the present value of the loan, the interest, and the time the loan will be paid out, respectively: "))
inter=float(input())
time=int(input())

fv=pv
for x in range(time):
    fv = fv+fv*(inter/12)
print(f"The total future value if no payments made and interest adds up after alloted time ({time}): " + "{:.2f}".format(fv)) 
print(f"At minimum, you will need to have a PMT of {math.ceil(fv/103)}")
 