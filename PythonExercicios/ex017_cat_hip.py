#import math
from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

#h = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa é {h}!')

#h = math.hypot(co, ca)
h = hypot(co, ca)

print(f'A hipotenusa é {h:.2f}!')
