


# Array in other progamins
# list in python is array in other

list1 = ['A', 'B', 'C']

#for i in list1:
    #print(i)

list1.append(13)

print(list1)

list1.remove(13)

print(list1)

list2 = [1,2,3]

list2 = list1.copy()

print('List 2 = ',list2)


# Difference b/w append() and extend()


myList = [1,2,3,4,5]

myList.append('ABC')

print(myList)


newList = [5,6,7,8]

myList.extend(newList)

print(myList)