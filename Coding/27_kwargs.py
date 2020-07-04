#use keyword-arguments keyword with double staric....
def my_func(**kwargs):
    return kwargs  #return dictionaries
result = my_func(name = "Ahad", roll = 48)
print(result)   #show dictionaries
print(f"Hi I am {result['name']}")  #show dictionaries value using keyword

#return tuple & dictionaries together
def my_func_one(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"Hi I am {kwargs['name']}, last in {args[3]}'s student")
my_func_one(10,20,30,40, name = "Ahad", roll = 48,sec = "A")
