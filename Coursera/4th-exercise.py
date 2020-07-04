hours = input("Enter Hours: ")
hrs = float(hours)
rate = input("Enter the Rate: ")
rt = float(rate)

def computepay(h,r):
    if h <= 40:
        pay = h * r
    elif h > 40:
        pay = 40 * r + (h-40)* 1.5 * r
    return pay


p = computepay(hrs,rt)
print("Pay",p)
