text = input("Enter any sentence or word... ")
def upper_lower(text):
    upper = 0
    lower = 0
    for char in text:
        if char.isupper():         #check upper case
            upper = upper + 1
        elif char.islower():       #check lower case
            lower = lower + 1
        else:
            pass
    length = len(text)
    print(f"The length of the \'{text}\' is {length}  &")
    print(f"upperCase: {upper}")
    print(f"lowerCase: {lower}")

upper_lower(text)
