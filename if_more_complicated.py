try:
    a = int(input("Give me a number pls"))
    b = int(input("Give me another number pls"))
except ValueError:
    print("One of the numbers was invalid")
else:
    if a > b:
    print(a, ">", b)
    elif a < b:
    print(a, "<", b)
    else:
    print(a, "=", b)
