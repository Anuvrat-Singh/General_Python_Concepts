tuple1 = (1,2,3,4,"anuvrat", "kumar", "singh",1,1,1,1,1,1,1)

print(len(tuple1))
print(tuple1[1])
print(tuple1.count(1))
print(tuple1.index("anuvrat"))

tuple2 = (20,30)
print(tuple2)

tuple3= tuple1 + tuple2
print(tuple3)

for i in tuple3:
    print(i)