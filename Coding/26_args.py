#use argument keyword with one staric when we need unknown number of arguments
def my_func(*args):
    return args #return arguments as a tuple

result = my_func(10,20)
print(result) #show tuple

#using arguments keyword for sevent arguments
def my_func_one(*args):
    return sum(args)
result = my_func_one(10,20,30,40,50,60,70)
print(result)
