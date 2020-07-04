input_number = int(input())
i= 0
phonebook = {}
while input_number > i :
    string_input = input()
    list_input = string_input.split()
    phonebook[list_input[0].lower()] = list_input[1]
    i = i + 1
i = 0
while input_number > i :
    match_name = input()
    if match_name == "EOF" :
        break
    match_name = match_name.lower()
    if match_name in phonebook:
        print(match_name + "=" + phonebook[match_name])
    else:
        print("Not found")
