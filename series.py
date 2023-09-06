'''
    1,10,20,30,40  Number - 5
   1,10,20,30,40,50
   1,10,20,30,40,50,60.
   1,10,20,30,40,50,60,70
   1,10,20,30,40,50,60,70,80



 0,10,20,30,40

 number = 1
 sec = 9 
 thrid= 9+11

'''
number = int(input("Pls input number"))
for  input in range(1,number):
    i =0
    series=0
    print("For value number is ", input, "Below series")
    while i<input:
        if i ==0:
            print(i+1,end=",")
        else:
            series =series + 10
            print(series,end=",")
        i = i+1
    print("")
