st = "The qick brown fox run over the little lazy dog."
print(st)
# find leng of string
print("leng ", len(st))

# 
# for i in (0,len(st)-1):
#     print(i, "String", st[i])

print(range(len(st))  )  
for i in range(10,20):
    print(i)

'''
range(starting, ending, by defalt step by 1)
range(starting, ending, step value)

'''
print("====================================")
s = 0
for i in range(10,20,2):
    print(i)
    s = s + i

print("Sum of series", s)

list_of_series = [ i for i in range(10,20,2)]
print("list of series ", list_of_series)
    
