# number = 3434
#           TH  H  T  O
# reverse = 4   3  4  3
number = int(input("Pls input the number"))
rev =0
cnt =0
while number>0:
    digit = number%10
#    sum = sum*10 +digit
    rev = rev*pow(10,cnt)+digit
    number = number//10
    cnt = cnt +1
    # print(digit , "- > number - ", number)
    print("rev", rev)