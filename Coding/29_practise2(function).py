def animal_crakers(text):
    word = text.split()         #create list using split function(space)
    first = word[0]             #store 1st character of the first item
    second = word[1]            #store 1st character of the second item
    if first[0] == second[0] :
        result = True
    else :
        result = False
    return result


result = animal_crakers("Labelheaded Llama")
print(result)
result= animal_crakers("Crazy kangaroo")
print(result)
