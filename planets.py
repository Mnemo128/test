#!/usr/bin/python3

planets = ['Merkur', 'Venus', 'Erde', 'Mars', 'Jupiter', 'Uranus', 'Saturn', 'Neptun']
vokale = 'aeiouAEIOU'
konsonanten = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'



for planet in planets:
    print(f'                    {planet}')
    for zeichen in planet:
        if zeichen in vokale:
            print(f'Vokal:      {zeichen} ')
        else:
            print(f'Konsonant:  {zeichen}')
