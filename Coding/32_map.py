def square(num):
    return num**2

myNums = [ 1, 2, 3, 4, 5]
List = list(map(square, myNums)) #work in every item of the list/tuple
print(List)
for item in List :
    print(item)
