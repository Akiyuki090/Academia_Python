x = int(input('Informe um lado: '))
y = int(input('Informe um segundo lado: '))
z = int(input('Informe um terceiro lado: '))

if x < y + z and y < x + z and z < y + x:
    print('Satisfaz a condição de existência')
else:
    print('Não satisfaz')  