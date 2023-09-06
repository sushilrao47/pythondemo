'''
    python : - list 
    list-> tuple
    touple->list
    empltiy-list> add the element
    

'''


mylist = list() # 
mytuple = tuple()
mylist.append("22")
mylist.append(1)
mylist.append("4")
mylist.append("252")
mylist.append("252")
print("List", mylist)
mytuple1 = list(mytuple)
mytuple1.append("22")
mytuple1.append(334)
mytuple1.append("4")
mytuple1.append("252")
mytuple1.append("252")
mytuple = tuple(mytuple1)
print("Tuple", mytuple1)
print("Tuple", mytuple)

newTuple=(1,4)
newTuple = newTuple+mytuple
print("Final Tuple", newTuple)

print("Check ", type(newTuple))
print("Check ", type(mylist))
##################
'''
tuple- (1)
'''
oneTuple=("stirng")
print("Onetuple", oneTuple, type(oneTuple))

oneTuple=(1,)
print("Onetuple", oneTuple, type(oneTuple))

####################################
'''
  for
  if
  base
  tuple,list,dic,map,filter
'''

'''
  dic - {key:value}
       {"Ram":"Nodia, UP"}

'''
# JSON
dictName={"Ram":"Nodia, UP", "Shyam":"Delhi", "abc":"dfa"}
dictName["ABCD"]="India"
print(dictName)
print("#######KEY and Value###############")
for key, value in dictName.items():
    print("key", key, "Value", value)

print("#########VALUE #############")
for value in dictName.values():
    print("key",value)
print("#########KEY #############")
for item in dictName:
    print("key",item)

print("#########based on key values #############")
for item in dictName:
    print("key",item,"-",dictName[item])
# dictName["abc"].append("Nodia1,")

