numList = list(input("enter the number of your choice :").split(","))
print("Given list is ", numList)


firstElement = numList[0]

lastElement = numList[-1]


if (firstElement == lastElement):
    print(True)
else:
    print(False)