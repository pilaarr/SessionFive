name = input("What is your name? ")
age = input("How old will you be this year? ")
try:
    age = int(age) # you get the age as a string and then you convert it to an integer
    birth_year = 2023 - age
    print("Sorry, that was not a valid number")
except NameError: # in case i wrote something wrong, e.g., integer() instead of int()
    print("oh, it's not you, it's me :)")
else: # do this in case there is no exception
    print(name, "you were born in", birth_year)
finally: # always executes at the end
    print("Thanks for playing, come again")