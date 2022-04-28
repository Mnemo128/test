#!/usr/bin/python3


uhrzeit = input('Bitte geben Sie die aktuelle Uhrzeit an: ')
uhrzeit = int(uhrzeit)


if uhrzeit <=7:
    print('Gute Nacht')
elif uhrzeit <= 11:
    print('Guten Morgen')
elif uhrzeit <=17:
    print('Guten Tag')
elif uhrzeit <=21:
    print('Guten Abend')
elif uhrzeit <=24:
    print('Gute Nacht')

