input_number = int(input())
if input_number % 2 == 0 :
    if input_number >= 2 and input_number <= 5 :
        print("Not Weird")
    elif input_number >= 6 and input_number <= 20 :
        print("Weird")
    elif input_number > 20 :
        print("Not Weird")
else:
    print("Weird")
