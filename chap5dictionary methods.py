myDict={
    "fast":"In a quick manner",
     "harry":" A coder",
     "marks":500,
     "anotherdict": {"harry":"aplayer"},
     "student": "Inamullah",
     1:2

}
print(type(myDict.keys()))#prints dict types of keys
print(type(myDict.values()))#print the type of class
print(list(myDict.keys()))#prints the keys
print(myDict.values())#prints the values
print(myDict.items())#print he key value for all items
updateDict = {
    "lovish":"Friend",
    "Divya":"clutch",
    "Shubham":"trend",
    "Harry":"A Dancer"
}
myDict.update(updateDict)#update the dictioary by adding Key:values pairs
print(myDict)

print(myDict.get("harry"))
print(myDict.get("Divya"))

#The difference between .get and[] syntax in dictioanry
print(myDict.get("harry2"))#this will return none while harry2 is not present in dictionary
print(myDict["harry2"])#Throws an error not present in dictioary

