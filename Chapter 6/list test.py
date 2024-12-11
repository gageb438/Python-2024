thislist = ["apple", "banana", "cherry"]
print(thislist[0])
print(thislist[1])
print(thislist[2])
print(thislist[-1])

print(thislist[0:2 + 1])

if "apple" in thislist:
    print("Apple is in this list")
    
thislist[1] = "potato"

print(thislist)

thislist[1:2] = "egg", "orange"

print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)