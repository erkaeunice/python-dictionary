student ={
  "FName"  : "Erka",
  "LName" : "Eunice",
  "Phone" : "0703768490",
  "Email":"ekaeunic@gmail.com"
}

print (student)

car ={
  "brand"  : "Ford",
  "model" : "Mustang",
  "year" : 1994,
  
}
x = car["model"]
print(x)

x=car.get("model")
print (x)


if "model" in car:
    print("Yes, 'model is one of the keys in the thisdict dictionary")

#change dictionary item
car ={
  "brand"  : "fOrd",
  "model" : "Mustang",
  "year" : 1896,

}
car ["year"] =2020 
print (car)


#adding an item to the dictionary 
car ={
  "brand"  : "fOrd",
  "model" : "Mustang",
  "year" : 1896,

}

car.pop("model")
print(car)
car.popitem()
print(car)
del  car["model"]
print(car)
car .clear()
print(car)

#loop through
car ={
  "brand"  : "fOrd",
  "model" : "Mustang",
  "year" : 1896,

}

for x in car:
   print(x)
for x in car.values():
  print(x)
for x in car.keys():
   print(x)

#neststed
child1= {
  "name":"erka",
  "year": 1998

}
child2= {
 "name":"joy",
 "year":2000

}
child3= {
 "name":"joy",
 "year":2000
}
myfamily= {
"child1" :child1,
"child2": child2,
"child3": child3
}
 
print (myfamily)


  

#adding an item to the dictionary 
car ={
  "brand"  : "fOrd",
  "model" : "Mustang",
  "year" : 1896,

}
car["color"] ="red"
print(car)

car["color"] ="red,blue,yellow,black,gree"
print(car)