#!/usr/bin/python3


# 192.168.0.0/16
# 172.16.0.0/12
# 10.0.0.0/8

#ipv4 = input('Bitte geben Sie eine IPv4 Adresse ein:  ')

adresse = True

gueltige_zeichen = ['0123456789.']

tests = [['192.168.2.23', True], ['1.2.3', False], ['172.16.2.26', True],['a.b.c.d', False], ['999.1.2.3', False], ['1..2.3', False], ['...', False],['-1.2.3.4', False], ['192.168.1.23/24', False], ['"1.2.3.4"', False], ["'1.2.3.4'", False]

def is_ipv4(ipv4):
    ipv4_1 = ipv4[0].split('.')
    if len(ipv4_1) != 4:
       # print('Fehlerhafte Eingabe')
       # exit(1)
        return False, ''

    gueltig= None
    for oktett in ipv4_1:
        if oktett == '':
            return False,''
        else:
            if gueltig is not False:
                gueltig = True

        if gueltig is False:
            return False,''

        oktett = int(oktett)
        if oktett >= 0 and oktett <= 255:
            pass
        else:
            adresse = False
            return False,'Wert ausserhalb des zulaessigen Bereichs'
     return ipv4_1,''


for test in tests:
    result, massage = is_ipv4(test)
    print(f'Test: {test}  ->  {result}  ->  massage: {massage}')
    print(is_ipv4(test))
