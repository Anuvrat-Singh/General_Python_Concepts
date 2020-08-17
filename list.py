email = "s.anuvrat@epharma.com"
substr = "epharma"

print(email.find(substr))
test="my name is anuvrat kumar singh is"
list1=test.split(" ")
print(len(list1))
print(list1)

for i in list1:
    if(i == "is"):
        print("yay")

print(list1[4])
print(list1[1:4])
list1.insert(1, 3.14)
print(list1)
list1.remove("is")
print(list1)
print(len(list1))
list2=[1,3,4]
print(len(list2))
list3 = list1 + list2
print(list3)
print(len(list3))