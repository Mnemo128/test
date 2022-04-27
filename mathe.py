#!/usr/bin/python3

text = input('Bitte geben Sie einen Text ein:    ')
a=1
b=2
c=a+b
print(f'   C enspricht: {c}')
print('a'*13)
with open('Mathe.txt', 'w') as fh:
    i=0
    while(i<1000):
        fh.write(text)
        i+=1
print('Rakamakafon')
