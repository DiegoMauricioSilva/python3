print('Olá, este simulador irá calcular o valor de sua prestação mensal, para o empréstimo bancário!')

vc = float(input('Digite o valor da casa: R$ '))
sc = float(input('Digite seu salário: R$ '))
a = int(input('Digite em quantos anos você deseja pagar: '))
pr = vc / (a * 12)

print(f'Para pagar uma casa de {vc}')

if pr <= (sc * 0.30):
    print(f'Empréstimo APROVADO, sua prestação mensal é R${pr}')
elif pr >= (sc * 0.30):
    print(f'Empréstimo NEGADO, sua prestação mensal seia de R${pr}')
