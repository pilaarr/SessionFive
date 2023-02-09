name = input("What is your name? ")
age = input("How old will you be this year? ")
age = int(age) # you get the age as a string and then you convert it to an integer
birth_year = 2023 - age
print(name, "you were born in", birth_year)