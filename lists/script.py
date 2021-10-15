myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print(myList[0])
print(myList[1])
print(myList[2])

print(myList)

for x in myList:
  print(x)

#Exercise

numbers = [1,2,3,]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]
mixed = [1, 'hello', 2.33, 'world']

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
print(mixed)

for item in mixed:
  print(item)