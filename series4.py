'''
  row-- 1 2 3 4 5 
        1 2 3 4 
        1 2 3
        1 2 
        1
'''
number = int (input("Pls input number"))
start =1
i=0
while i<number:
    for s in range(1, number+1-i): # range(startin,ending) ->  staring, ending-1
        print(s,end=" ")
    i = i+1
    print("")