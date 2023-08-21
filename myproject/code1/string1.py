st = "This quick brown fox jump over the little lazy dog."
print(st )
print(st[0:])
print(st[5:])
print(st[:])
print(st[-5:], len(st[-5:]))
print(st[-10:], len(st[-10:]))
print(st[::-1])

print(st[::-2])


for i in range(len(st)):
    print(st[i], end="-")

print("\n")
for i in range(len(st)):
    print(st[i], end="%")

print("\n")
for i in range(len(st)-1,-1,-1):
    print(st[i], end="")




print("\n")
rev = ["".join(st[i]) for i in range(len(st)-1,-1,-1)]
print("Rev ", rev)


# abc, this
# abcthis
st1= "how are you"
st2= "I am good"
st3 = st1+st2
print(st3)

# abc, this
# abcthis
st1= "how are you"
st2= "I am good"
st3 = "".join([st1,st2]) # when use this
print(st3)

# abc, this
# abcthis
st1= "how are you"
st2= "I am good"
st3 = "%s%s"% (st1,st2)  # when we use 
print(st3) 

# abc, this
# abcthis
st1= "how are you"
st2= "I am good"
st3 = "{}-{}".format(st1,st2) 
print(st3) 
