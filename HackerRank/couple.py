input_number = int(input())
list_string = input()
list_item = list_string.split()

number = 0
couple = {}
for item in list_item:
    if item not in couple:
        couple[item] = 1
    else:
        couple[item] = couple[item] + 1
        if couple[item] == 2 :
            number = number + 1
            couple[item] = 0
print(number)
