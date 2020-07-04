#list
my_list = ["One", "Two", "Three", "Four"]
print(my_list)

#indexing
print(my_list[0])
print(my_list[1:])

#add a new list
another_list = ["Five", "Six"]
new_list = my_list + another_list
print(new_list)

#append function
new_list.append("Seven")
print(new_list)

#pop function
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

#inserting an item
new_list.insert(5,"eight")
print(new_list)

#delete item from 3 to 5
del new_list[3:5]
print(new_list)

#Sorting -------
list = [1, 2, 3, 8, 5]
list.sort()
print(list)

#reverse ------
list.reverse()
print(list)
