input_number = int(input())
string_input = input()
i = 0
sum = 0
valey = []
for char in string_input:
    if char.lower() == "u":
        i = i + 1
        if i > 0:
            sum = sum + 1
        valey.append(i)
    if char.lower() == "d":
        i = i - 1
print(sum)
