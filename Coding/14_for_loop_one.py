myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print the item of the list
print("The items of the list are : ")
for num in myList:
    print(num)

#print the even number of the list
print("The Even Numbers are : ")
for num in myList:
    #check Even
    if (num % 2 == 0):
        print(num)

#print the sum of the item of the list
sum = 0
for num in myList:
    sum = sum + num
print(f"The Sum of the list is : {sum}")
