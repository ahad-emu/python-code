#creating item(tuple) in list using enumerate function
word = "abcde"
li = list(enumerate(word))
print(li)

#finding index postion with item
word = "ABCDE"
for item,value in enumerate(word):
    print(f"The {item} index item is :\'{value}\'")
