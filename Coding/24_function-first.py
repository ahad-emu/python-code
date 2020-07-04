#print without argument & no return
def my_func():
    print("Hello!!")
my_func()

#print with argument & no return
def my_func_01(name):
    print("hello " + name)
my_func_01("Ahad")

#print with argument & return sum
def my_func_02(a,b):
    return a+b
result = my_func_02(10,20)
print(result)
