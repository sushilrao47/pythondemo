# number = 6
'''

6! = 6*5*4*3*2*1 ---  a*b
   = 1*2*3*4*5*6 ---- b*a
'''


number = int(input("Input number"))
fact=1
print(number, end="")
while(number>0):
     fact = fact*number
     number = number-1
print( "! = ", fact)
