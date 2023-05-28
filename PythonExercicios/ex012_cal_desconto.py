p = float(input('Qual o valor do produto: R$ '))
d = float(input('Qual o valor do desconto em percentual é: '))
pf = p - (p * d/100)
print(f'O produto custava R${p}, na promoção com o desconto {d}%, vai custar R${pf:.2f}.')


