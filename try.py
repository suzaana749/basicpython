try:
    file = open("test file","w")
    try:
        file.write("written here")
    finally:
        print("abcd")
        file.close()
except IOError:
    print("error")