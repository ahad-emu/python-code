hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hrs = int(hours)
    rt = float(rate)
    if hrs >= 40:
        pay = 40 * rt + (hrs-40) * (1.5 * rt)
    else:
        pay = hrs * rate
    print(pay)
except:
    print("Error, please enter numeric input")
