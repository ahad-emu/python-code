input_loop = int(input())

for i in range(0, input_loop):
    number = int(input())
    if number < 40 :
        result = 40 - number
        if result > 2:
            result = number
        else:
            result = 40
    elif number < 45:
        result = 45 - number
        if result > 2:
            result = number
        else:
            result = 45
    elif number < 50:
        result = 50 - number
        if result > 2:
            result = number
        else:
            result = 50
    elif number < 55:
        result = 55 - number
        if result > 2:
            result = number
        else:
            result = 55
    elif number < 60:
        result = 60 - number
        if result > 2:
            result = number
        else:
            result = 60
    elif number < 65:
        result = 65 - number
        if result > 2:
            result = number
        else:
            result = 65
    elif number < 70:
        result = 70 - number
        if result > 2:
            result = number
        else:
            result = 70
    elif number < 75:
        result = 75 - number
        if result > 2:
            result = number
        else:
            result = 75
    elif number < 80:
        result = 80 - number
        if result > 2:
            result = number
        else:
            result = 80
    elif number < 85:
        result = 85 - number
        if result > 2:
            result = number
        else:
            result = 85
    elif number < 90:
        result = 90 - number
        if result > 2:
            result = number
        else:
            result = 90
    elif number < 95:
        result = 95 - number
        if result > 2:
            result = number
        else:
            result = 95
    elif number <= 100:
        result = 100 - number
        if result > 2:
            result = number
        else:
            result = 100

    print(result)
