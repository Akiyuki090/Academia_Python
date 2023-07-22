x = int(input('Informe um lado: '))
y = int(input('Informe um segundo lado: '))
z = int(input('Informe um terceiro lado: '))

if x < y + z and y < x + z and z < y + x:
    if x == y and y == z:
        print("Equilátero")
    elif x == y or y == z or z == x:
        print('Isósceles ')
    else:
        print('Escaleno')
else:
    print('Não satisfaz')  