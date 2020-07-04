string_input = input()
list_input = string_input.split(":")

list_input[0] = int(list_input[0])
letter = list_input[2][2:3]
if letter.lower() == 'p' and list_input[0] != 12:
    list_input[0] = list_input[0] + 12

if list_input[0]==12 and letter.lower() == 'a':
    list_input[0] = 0

if list_input[0] >= 10 :
    list_input[0] = str(list_input[0])
elif list_input[0] == 0:
    list_input[0] = "00"
else:
    list_input[0] = "0" + str(list_input[0])

list_input[2] = list_input[2][0:2]

string_output = ":".join(list_input)
print(string_output)
