'''

8. 123 - 1^3+2^3+3^3
    = 1^3 + 2^3 +3^3


'''
number = int(input("Pls input number"))
s =0
while number>0:
    digit = number%10
    print(digit,"^3", end="+")
    s = s + pow(digit,3)
    number = number//10

print( "=",s)