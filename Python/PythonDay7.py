#collections --> list ordered and mutable []
fruits=["apple","banana","cherry"]
print(dir(fruits))
#adding element to list
fruits.append("orange")
print(fruits)
#remove
fruits.remove("orange")
print(fruits)
#reverse
fruits.reverse()
print(fruits)
#insert
fruits.insert(2,"guava")
print(fruits)
#popping last element
fruits.pop()
print(fruits)
#counting element
print(fruits.count("banana")) 

#collections -->tuple ordered and immutable ()
color=("red","green","blue")
print(color[2])
print(color)
print(dir(color))
print(color.count("red"))

#collections -->set unordered and unindexed {}
animals={"dog","cat","rabbit"}
print(animals)
animals.add("cow")
print(animals)
animals.remove("cat")
print(animals)

#2d list
matrix =[
    [1,2],[3,4],[44,45]
]
print(matrix)

print(matrix[0][1])