print("range(stop)")
for num in range(10):
    print(num) #print 0 1 2 3 4 5 6 7 8 9

print("range(start,stop)")
for num in range(3,10):
    print(num) #print 3 4 5 6 7 8 9

print("range(start, stop, step)")
for num in range(1,10,2):
    print(num) #print 1 3 5 7 9


print("initialize in array using range operator")
array_list = list(range(0,11,2)) #list function
print(array_list) #print array_list(variable) 0 2 4 6 8 10
