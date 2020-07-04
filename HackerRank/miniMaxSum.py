input_string = input()
input_list = input_string.split()

list_min_max = []
for item in input_list:
    list_min_max.append(int(item))

length_of_list = len(list_min_max)

sum_of_min = 0
sum_of_max = 0

for item in range(0, length_of_list-1):
    sum_of_min = sum_of_min + list_min_max[item]

for i in range(0, length_of_list):
    sum = 0
    for j in range(0, length_of_list):
        if i == j:
            continue
        else:
            sum = sum + list_min_max[j]

    if sum > sum_of_max:
        sum_of_max = sum
    if sum < sum_of_min:
        sum_of_min = sum


print(f"{sum_of_min} {sum_of_max}")
