n1 = int(input('Digite o primeiro número a comparar: '))
n2 = int(input('Digite o segundo número a comparar: '))

if n1 > n2:
    print(f'O PRIMEIRO número {n1} é MAIOR que {n2}')
elif n2 > n1:
    print(f'O SEGUNDO número {n2} é MAIOR que {n1}')
elif n1 == n2:
    print(f'Não existe número maior, os números {n1} e {n2} são iguais!')
