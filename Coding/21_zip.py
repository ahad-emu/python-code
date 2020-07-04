mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']

#two list zip together
list3 = list(zip(mylist1, mylist2))
print(list3)

#print two list as a tuple
for item in zip(mylist1, mylist2):
    print(item)

#print one value of the tuple in zip function
for item,value in zip(mylist1, mylist2):
    print(value)
