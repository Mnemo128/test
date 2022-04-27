#!/usr/bin/python3


####Introduction

print(20*'\n','- P E R S O N E N - E R F A S S U N G S - S O F T W A R E - \n -MarkusMichaelLedwig\n',80*'_')
print(' Mithilfe dieser Software können Sie Personen mit Vor- und Nachnamen erfassen.\n Die Namenpaare werden anschließend in der Datei "Personen.txt" gespeichert.\n Diese befindet sich in dem Verzeichnis in dem die Software ausgeführt wurde.\n Die Software ermöglicht ebenfalls das Betrachten der angelegten Text Datei.\n',80*'_',20*'\n')


####Menu


wahl=''
while (wahl != 'Q'):
    wahl=input('\n\nWählen Sie einen der folgenden Menuepunkte: \n \n -Person erfassen  -> Druecken Sie:  A \n -Liste anzeigen   -> Druecken Sie:  B \n -Beenden          -> Druecken Sie:  Q  \n\n\n\n\n\n\n\n\n\n\n\n\nAuswahl:   ').upper()
    while wahl !='A'and wahl !='B' and wahl!='Q':
        print(5*'\n',31*'_','Warnung',40*'_',5*'\n','\nUngueltige Eingabe.\n',5*'\n',80*'_',5*'\n')
        break


#####Erfasst Person und zeigt Ergebnis


    if wahl =='A':
        print(10*'\n','- P E R S O N E N - E R F A S S U N G S - S O F T W A R E - \n -MarkusMichaelLedwig\n',80*'_')
        print(10*'\n',80*'_','\n','Um eine Person zu erfassen benoetigt man Vor- und Nachnamen.','\n',80*'_',25*'\n')
        persons = []
        Vorname = input('Bitte geben Sie zunaechst einen Vornamen ein:  ')
        Nachname = input('Bitte geben Sie nun einen Nachnamen ein:  ')
        person ={'Vorname': Vorname,'Nachname': Nachname }
        persons.append(person)
        print(10*'\n','- P E R S O N E N - E R F A S S U N G S - S O F T W A R E - \n -MarkusMichaelLedwig\n',80*'_',10*'\n')
        print(f'\nDie Person " {Vorname} {Nachname} " wurde wie folgt registriert:\n')
        for person in persons:
            print(80*'_','\n')
            print(f'Vorname: {person["Vorname"]}')
            print(f'Nachname: {person["Nachname"]}')#


####In Txt Datei schreiben


        with open('Personen.txt', 'a') as file_handle:
            file_handle.write(str(persons))
            print(80*'_')
            print('\nSchreibe....\n\n')
            print('...Person wurde in Liste ("Personen.txt") übertragen!\n')
            print(80*'_')

######Zeigt Inhalt der abgespeicherten Liste an


    if wahl =='B':
        print(2*'\n','- P E R S O N E N - E R F A S S U N G S - S O F T W A R E - \n -MarkusMichaelLedwig\n',80*'_')

        print('Die Liste einthält folgende Daten: ')
        with open('Personen.txt', 'r')as file_handle:
            line= file_handle.read().split('[')
            for person in line:
                print(person)
        print(2*'\n',80*'_',10*'\n')



#######Beenden des Programms---Abschiedsnachricht



print(20*'\n','- P E R S O N E N - E R F A S S U N G S - S O F T W A R E - \n -MarkusMichaelLedwig\n',80*'_')
print(10*'\n','Das Programm wurde beendet.\n Auf Wiedersehen.')

print(22*'\n')
