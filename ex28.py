turno = input("Em que turno você estuda?\n M - Matutino \n V - Vespertino \n N - Noturno  \n :")

if turno == 'M':
    print(f'Bom Dia!')
elif turno == 'V':
    print(f'Boa Tarde!')
elif turno == 'N':
    print(f"Boa Noite!")
else:
    print(f'TURNO INVÁLIDO')