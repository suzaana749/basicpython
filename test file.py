# try:
#     file = open("test file","w")
#     file.write("file opened")
# except IOError:
#     print("IO error")
# else:
#     print("file closed")
#     file.close()

# try:
#     file = open("test file","r")
#     file.write("file opened")
# except IOError:
#     print("IO error")
# else:
#     print("file closed")
#     file.close()

try:
    file = open("test file","w")
    file.write("file opened")
finally:
    print("written")
    file.close()