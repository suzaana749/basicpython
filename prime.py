from __future__ import print_function
num = 90
prime = True
for text in range(2,num):
    if(num %text == 0 and num !=text):
        print(num,'equal',text,'*',num/text)
        prime= False
        break
    else:
        print(num,'is a prime number')
    if prime:
         print(num,'is a prime number')
    else:
        print(num, 'is not a prime number')





