#dictionary
my_dict = {
    "Name": "Ahad",
    "Roll": "048",
    "Sec": "A"
}
print(my_dict)
print(my_dict["Name"])

#assign value
my_dict["Name"] = "Emu"
print(my_dict)

#add a property
my_dict["Age"] = 22
print(my_dict)

#List & another dictionary in one dictionary
dict_list = {
    "k1": [1,5,3],
    "k2": {"Name": "Ahad", "Roll":"048"}
}

print(dict_list)
dict_list["k1"].sort()
print(dict_list["k1"])
