#odd = str(input("enter any number of your choice by comma separated  : ").split(","))
#even = str(input("enter any number of your choice by comma separated : ").split(","))

#print(int(odd))
#print(int(even))

odd = [10, 20, 23, 11, 17]

even = [13, 43, 24, 36, 12]
print(odd)
print(even)

list1=[]

for num in odd :
    if (num % 2 != 0) :
        list1.append(num)

for num in even :
     if(num % 2 == 0) :
        list1.append(num)

print ("result of new list is : " )
print(list1)       