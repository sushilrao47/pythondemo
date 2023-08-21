# list,  tuple and dict
l = [1,2,3,4,4,5,6,7,7]
t = (1,2,3,4,5,6,7)
d = {"name":12323, "address": "delhi"}
print("list ", l)
print("Tuple", t)
print("Dic", d)
for i in d:
     print("key",i,", Value:", d.get(i))