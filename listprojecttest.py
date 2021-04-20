

# Wanna check whether item is in shop or not

list1 = ["Soap", "Match Box", "Pen"]

print(list1)

item = input("Name of item yuou want to update ")

if item in list1:
    i = input("New Item Name ")

    index = list1.index(item)

    list1.insert(index, i)

    list1.remove(item)

print(list1)