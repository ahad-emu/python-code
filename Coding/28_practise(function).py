def lessers_of_two_even(a,b):
    if a%2==0 and b%2==0 :
        if a<b :            #when both are even show the smallest integer
            return a
        else :
            return b
    else :
        if a>b :            #when both are not even then show the biggest integer
            return a
        else :
            return b

number = lessers_of_two_even(2,4)
print(number)
number = lessers_of_two_even(2,5)
print(number)
