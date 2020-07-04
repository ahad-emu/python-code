Data = [2, 5, 9, 75, 17, 55, 3 ]

MAX = Data[0]
LOC = 0
i = 0

N = len(Data)
while True :
    i = i + 1
    if i >= N :
        break

    if MAX < Data[i] :
        LOC = i
        MAX = Data[i]


print(f"The largest element is {MAX}\n")
print(f"The Location of the largest element is {LOC + 1}")
