#comments - line and block (documentaiton)
'''
    Documentation 
    # Purspose of this program
    # Addition of two number
    Step : first two value , 
'''
import math
a = float(input("Enter value first :"))
b = float(input("Enter value sec:"))
print("a",type(a),"b", type(b))
sum = a + b
print("Sum of a +b", round(sum,4))
# Floor and ceil
print("Floor value of ",math.floor(a))
print("Ceil value of ",math.ceil(a))
a +=a # a = a +a
print(a)

# Assignment operator 
# what is assignment operator,  = is assigment operator 
# what is purpose of assignemtn opertor
a =34
#a,b=4 # this canot be unpacked
# b =34
# a = a+b
a +=a # a = a +a
print(a)
a *=a # * multiple
     # a = a *a
print("Mult of a ",a)
a=34
b=2

# a /=b# a = a/b
a %=b# % this modulo, it mean reminder
print("Mult of a ",a)


# Arithmetic operator  +,-,*,/,%