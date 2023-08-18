'''number=234
first = number%10 # 4
sec = number//10 # 123

next = sec%10 # 3
step2 = sec//10# 12

next1 = step2%10 # 2
last = step//10 # 1

sum = last+next1+next+first
# the number we are deling is decimal number, it mean base of number is 10 that is why we are divide by 10
Binary = 2
octal = 8
hexdec = 16
dec =10
'''
# logic 
number = int(input("Pls input the number"))
sum =0
while number>0:
    digit = number%10
    sum = sum +digit
    number = number//10
    # print(digit , "- > number - ", number)
print("sum", sum)