#!/usr/bin/python3



liste=[]
satz = input('Bitte gebe Sie einen Satz ein: ')
wort = ''



for zeichen in satz:
    if zeichen != ' ':
         wort = wort + zeichen
### umkehren  ###################
#        wort = zeichen + wort
#################################
    else:
         liste.append(wort)
         wort = ''
satz.append(wort)



print(liste)
