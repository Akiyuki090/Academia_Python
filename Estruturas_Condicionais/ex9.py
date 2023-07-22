idade = int(input('Qual a idade: '))

match idade:
    case i if 0 <= i <= 12:
        print('Criança')
    case i if 13 <= i <= 18:
        print('Adolescente')
    case i if i >= 19:
        print('Adulto')
    case _:
        print('Idade inválida')
