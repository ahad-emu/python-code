def check_even(num):
    return num%2==0

myNums = [1, 2, 3, 4, 5, 6]
list = filter(check_even,myNums)        #work in only return true based item of the list/tuple

for item in list:
    print(item)
