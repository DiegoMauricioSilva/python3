nome = str(input('Digite seu nome: '))
serie = int(input('Digite sua série: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota:'))
m = (n1 + n2 + n3)/3
prox = serie + 1

if m >= 7:
    print(f'Parabéns, {nome}! Sua média foi {m}')
    print(f'Seja Bem-vindo (a), {nome} a {prox} série escolar.')
elif m <= 6.99:
    print(f'Que pena {nome}, sua média foi {m}, não desanime {nome}, tente de novo!')




