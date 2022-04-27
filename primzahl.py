#!/usr/bin/python3





#Schleife die Zahlen unter 100.000 betrachtet

staer_wert = 4
end_wert = 31
prime_list = [ 2, 3 ]


for teste_zahl in range(start_wert, end_wert):
    for teiler in range(2, teste_zahl):
        print(f'Teiler {teiler}')
        if teste_zahl % teiler == 0:
            print(f'Keine Primzahl  {teste_zahl} % {teiler}')
            break
        if teiler == teste_zahl-1:
            prime_liste.append(teste_zahl)
            print(f'{teste_zahl} appendet - {teiler}')


print(prime_list)
