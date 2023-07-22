import math

numero = int(input('Qual o número: '))

if numero <= 1:
    print("Não é primo")
else:
    eh_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("É primo")
    else:
        print("Não é primo")
