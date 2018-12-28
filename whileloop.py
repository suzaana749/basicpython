from __future__ import print_function
num = 7
text = 3
prime = True
while text< num:
    if(num %text == 0 and num !=text):
        print(num,'equal',text,'*',num/text)
        break
    else:
        print(num, 'is not a prime number')
    text = text+1

