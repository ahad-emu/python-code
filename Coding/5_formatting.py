#------Normal------
Name = "Ahad"
print("Hello " + Name)


#-----.format()-----
my_string = "hello world"
print("The world is {}".format("beautyfull"))

result = 100/770
print("The result is : {r:1.3f}".format(r = result))

print("{} {} {}".format("Ahad", "Emu", "Antu"))
A = "Ahad"
E = "Emu"
N = "Antu"
print("{} {} {}".format(A, E, N))
print("{1} {2} {0}".format("Ahad", "Emu", "Antu"))
print("{A} {N} {E}".format(A="Ahad", E="Emu", N="Antu"))

#-----f-string format----
my_string = "Ahad"
print(f"Hello {my_string}")
