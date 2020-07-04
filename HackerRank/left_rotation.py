insert_string = input()
insert_list = input()
number_list = insert_string.split()
N = int(number_list[0])
d = int(number_list[1])

list_item = insert_list.split()

for i in range(0, d):
    item = list_item[0]
    list_item.pop(0)
    list_item.append(item)

output = " ".join(list_item)
print(output)
