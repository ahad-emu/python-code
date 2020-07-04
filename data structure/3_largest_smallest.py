Data = [2, 5, 9, 75, 17, 55, 1 ]

MAX = Data[0]
MIN = Data[0]
LOC_max = 0
LOC_min = 0
i = 0

N = len(Data)
while True :
    i = i + 1
    if i >= N :
        break

    if MAX < Data[i] :
        LOC_max = i
        MAX = Data[i]
    if  MIN > Data[i] :
        LOC_min = i
        MIN = Data[i]


print(f"The largest element is {MAX}\n")
print(f"The Location of the largest element is {LOC_max + 1}\n")
print(f"The smallest element is {MIN}\n")
print(f"The Location of the smallest element is {LOC_min + 1}")
