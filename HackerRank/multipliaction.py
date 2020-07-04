string_input = input()
integer_input = int(string_input)

for i in range(1, 11):
    multiplication = i * integer_input
    print(f"{integer_input} x {i} = {multiplication}")
