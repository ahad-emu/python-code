lists = [1, 2 , 3, 4, 5]
#return true or false
bool = 2 in lists
print(bool)   #true
bool = 'x' in lists
print(bool) #false

#in keyword using in dictionaries
dict = {'key1' : 123, 'key2' : 321}
bool = 'key1' in dict
print(bool) #true
bool = 123 in dict.values()
print(bool) #true
