


list1=["Ayaz","Turab","Ayoob"]

print(list1)

item=input("Enter the item you want to update:  ")

if item in list1:

    i=input("enter the new name:    ")
    
    index=list1.index(item)

    list1.insert(index,i)

    list1.remove(item)

print(list1)