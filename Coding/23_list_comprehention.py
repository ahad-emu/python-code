word = "abcde"
mylist1 = []
for letter in word:
    mylist1.append(letter)
print(mylist1)
#---------------------------------
#[operation for variable in object condition]
mylist2 = [letter for letter in word]
print(mylist2)

#for cube
cube = [i**3 for i in range(1,11)]
print(cube)

#for if-else condition
even = [num for num in range(1,21) if num%2==0]
print(even)

#for expression
fahrenhiet = [32, 50, 68]
celsius = [((num-32)/9)*5 for num in fahrenhiet]
print(celsius)
