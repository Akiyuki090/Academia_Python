import math


a = float(input('Informe o coeficiente angular: '))
b = float(input('Informe o coeficiente linear: '))
c = float(input('Informe a constante: '))

delta = pow(b, 2) - 4 * a * c

if delta > 0:
    print('Duas raízes reais: ')
    raiz1 = (-b + round(math.sqrt(delta), 2))/ 2 * a
    print(raiz1)
    raiz2 = (-b - round(math.sqrt(delta), 2))/ 2 * a
    print(raiz2)

elif delta == 0:
    print('Uma raíz nos reais: ')
    raiz = -b/(2*a)
    print(raiz)
else:
    print("Não existe raíz nos reais")