nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

media = round((nota1 + nota2 + nota3) / 3, 1)
print(media)

if media >= 7:
    print('Aprovado')
elif 4 <= media and media < 7:
    print('Recuperação')
else:
    print('Reprovado')
