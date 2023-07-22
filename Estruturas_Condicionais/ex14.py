salario = float(input('Qual o salário: R$'))

if salario > 1500:
    reajuste = salario + (salario * 0.1)
    print(reajuste)
else:
    reajuste = salario + (salario * 0.15)
    print(reajuste)
    