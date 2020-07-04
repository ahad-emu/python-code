counter_input = int(input())
for counter in range(0, counter_input):
    string_input = input()
    length = len(string_input)
    even_string = ""
    odd_string = ""
    for i in range(0, length):
        if i % 2 == 0:
            even_string = even_string + string_input[i]
        else:
            odd_string = odd_string + string_input[i]

    print(f"{even_string} {odd_string}")
