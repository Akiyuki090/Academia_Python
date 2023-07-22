x = int(input('Informe um numero: '))
y = int(input('Informe um segundo numero: '))
z = int(input('Informe um terceiro numero: '))

if x > y and x > z:
    print(f'Maior valor: {x}')
elif y > x and y > z:
    print(f'Maior valor: {y}')
else:
    print(f'Maior valor {z}')
     