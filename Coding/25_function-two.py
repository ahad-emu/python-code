#function with build-in function sum()
def my_func(a,b):
    return sum((a,b))
result = my_func(50,10)
print(result)

#function with default arguments
def my_func_one(a,b,c=0,d=0, e=100):
    return sum((a,b,c,d,e))

result = my_func_one(10,20)
print(result)
result = my_func_one(10,20,20)
print(result)
result = my_func_one(10,20,20,20)
print(result)
result = my_func_one(10,20,20,20,20)
print(result)
