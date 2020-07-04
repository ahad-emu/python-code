input_string = input()
integer_input = input()
N = int(integer_input)
count = 0
length = len(input_string)
for char in input_string:
    if char is "a":
        count = count + 1

division = N/length
number = round(division*count)
print(number)
