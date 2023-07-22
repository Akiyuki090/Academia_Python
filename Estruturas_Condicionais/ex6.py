# 18.5 ate 24.9, normal, 25 ate 29.9, sobrepeso, >30 obesidade

altura = float(input('Informe a altura em metros: '))
peso = float(input('Informe o peso em quilos: '))

imc = round((peso/pow(altura, 2)), 1)

print(imc)

if imc <= 18.4:
    print('Subpeso')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal')
elif imc >= 25 and imc < 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')