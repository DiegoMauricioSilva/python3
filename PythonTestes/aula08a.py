import math
import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} arredondando para cima é {math.ceil(raiz)}')
print(f'A raiz de {num} arredondando para baixo é {math.floor(raiz)}')
print(f'A raiz de {num} sem arredondamento é {raiz:.2f}')
print(emoji.emojize('Olá, Mundo :sunglasses:', use_aliases=True))
