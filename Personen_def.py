#!/usr/bin/python3

# T E S T E I N T R A G

import os
import lib.Personen_def_modul as p
file_data = 'Personen.csv'
file_data2='Personen.json'
persons = []

action = ''

while action != 'q':
    print('_'*80)
    print('Personen E R F A S S E N: (A) ')
    print('Personen A N Z E I G E N: (B)')
    print('Personen S P E I C H E R N: (C)')
    print('Personenliste E I N L E S E N: (D) ')
    print('Programm B E E N D E N: (Q)')
    print('_'*80)
    action = input('Waehlen Sie einen Menuepunkt aus: ')

    if action == 'a':
        p.erfassen(persons)
    if action == 'b':
        p.anzeigen(file_data, persons)
    if action == 'c':
        p.speichern(file_data2, persons)
        p.speichern(file_data, persons)
    if action == 'd':
        p.einlesen(file_data, persons)
    if action == 'q':
        exit()
    
