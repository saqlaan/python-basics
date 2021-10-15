phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
  print("Phone number of %s is %d" % (name, number))

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
data = [1,2,3,4,5]
data.pop()
print(data)

phonebook = {  
    "John" : 938477566,
    "Saqlain" : 'Jill',
    "Jills" : 947662781
}  

if "Saqlain" in phonebook: 
  print("Saqlain is listed in the phonebooks")

if "Jill" not in phonebook:
  print("Jill is not in the phonebook")