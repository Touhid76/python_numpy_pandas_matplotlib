#list method in python
li=[1,2,3,4,5]
#append method
li.append(6)
print(li)

#copy method
li2=li.copy()
print(li2)

#sort method
li3=[3,1,4,2,2,5]
li3.sort()
print(li3)
#reverse method
li3.reverse()
print(li3)

#count method
print(li3.count(2))

#extend method
li4=[7,8,9]
li5=[10,11,12]
li4.extend(li5)
print(li4)

#pop method-index likhte hoy pop er modhe
li4.pop(1)
print(li4)

#insert method
li4.insert(1,8)
print(li4)

#remove method-jodi multiple same number thake taile first tare remove korbe
li4.remove(8)
print(li4)

#clear method
li4.clear()
print(li4)

