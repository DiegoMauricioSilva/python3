print('-=' * 25)
print('Analisador de triângulos')
print('-=' * 25)

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos {r1}, {r2} e {r3} podem formar um triângulo!')

    if r1 == r2 == r3:
        print('O triângulo formado é EQUILÁTERO: todos os lados são iguais.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado é ISÓSCELES: possui dois lados iguais e um diferente.')
    else:
        print('O triângulo formado é ESCALENO: todos os lados são diferentes.')
else:
    print(f'Os segmentos {r1}, {r2} e {r3} não podem formar um triângulo!')
