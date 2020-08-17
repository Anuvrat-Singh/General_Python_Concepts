
for i in range(10):
    print(i)
#for with final range
inputRange = input("Enter limit --->")

for i in range(int(inputRange)):
    print(i)

#for with initial and final range

table = input("Enter number to print the table --->>> ")

for i in range(1,11):
    print(table + " * " + str(i) + " = " + str(int(table)*i))