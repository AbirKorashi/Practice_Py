#Collection = single"Variable" used to store multiple values
#List = [] Ordered & changeable .Duplicate ok
#Sets = {} Unoedered & Mutable . But add /Remove Ok .No Duplicate
#Tuples = () Ordered & changeable .Duplicate Ok .Faster

fruites =["apple","Orange","banana","coconut"]

print(dir(fruites))
#print(help (fruites))

print(fruites[3])
print(fruites[:3])
print(fruites[::2])
print(fruites[::-1])

fruites.append("pineapple")
print(fruites)

fruites.remove("apple")
print(fruites)

fruites.insert(0,"jackfruit")
print(fruites)

fruites.sort()
print(fruites)

fruites.reverse()
print(fruites)

# fruites.clear()
# print(fruites)
#
# print(fruites.index("apple"))
#
# fruites.count("banana")

fruites ={"apple","Orange","banana","coconut"}
print(fruites)

print(fruites.add("pineapple"))

print(fruites.remove("apple"))
print(fruites.pop())
print(fruites.clear())