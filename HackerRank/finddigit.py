loop_control = int(input())
for item in range(0,loop_control):
    input_string = input()
    input_list = []

    for item in input_string:
        input_list.append(int(item))

    digit = []

    for item in input_list:
        if item not in digit:
            digit.append(item)

    print(len(digit))
