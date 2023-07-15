nome1 = str(input('Digite seu nome: '))
nascimento1 = int(input('Qual o ano do nascimento: '))

nome2 = str(input('Digite seu nome: '))
nascimento2 = int(input('Qual o ano do nascimento: '))

diferenca = nascimento1 - nascimento2

print(f'A diferença de idade entre {nome1} e {nome2} é de: {abs(diferenca)} anos')
