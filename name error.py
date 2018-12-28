
while True:
    try:
        print("let us solve the equation(x/2)/(x-y)")
        x = float(input("enter value for x:"))
        y = float(input("enter value for y:"))
        if x == 0 or y == 0:
            break
        z = (x / 2) / (x - y)
    except Exception as e:
        print(str(e))
    except ZeroDivisionError as e:
        print("there was an error with code")
        print("you keyed in a value that was caused a division by zero")
    except NameError as e:
        print("there was an error with code")
        print("you keyed in a text value where a number was expected")
    else:
        print("solving(x/2)/(x-y) for value =", x, "and y", y, "we get the result ", z)
    finally:
        print("clean up code goes here")


