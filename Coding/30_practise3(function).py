def makes_twenty(a,b):
    if a == 20 or b == 20 :
        return True             #if any one item is 20 , return true
    elif (a+b)==20 :
        return True             #if the summation of two item is 20, return true
    else :
        return False
result = makes_twenty(20,10)
print(result)
result = makes_twenty(2,18)
print(result)
result = makes_twenty(2,130)
print(result)
