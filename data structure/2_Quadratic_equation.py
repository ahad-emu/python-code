A = int(input("Enter the value of A\n"))
B = int(input("Enter the value of B\n"))
C = int(input("Enter the value of C\n"))

D = (B*B) - (4*A*C)

if D > 0 :
    X1 = (-B + D**(1/2))/(2*A)
    X2 = (-B - D**(1/2))/(2*A)

    print(f"The Two Distinct Real Solution is X1 = {X1} and X2 = {X2}")
elif D == 0 :
    X = -B / (2*A)
    print(f"The Real Solution is X = {X}")
else :
    print("No Real Solution")
