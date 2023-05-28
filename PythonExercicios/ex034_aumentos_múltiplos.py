sal = float(input('Qual é o salário do funcionário: R$'))

if sal <= 1249:
    sal = sal * 1.15
    print(f'Parabéns, com seu aumento de 15%, você agora irá receber R${sal}')
else:
    sal = sal * 1.10
    print(f'Parabéns, com seu aumento de 10%, você agora irá receber R${sal}')
