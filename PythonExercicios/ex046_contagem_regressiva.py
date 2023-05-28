import time

print('Contagem regressiva para o estouro de fogos de artifício:')

for i in range(10, -1, -1):
    print(i)
    time.sleep(0.75)

print('BOM, BOM, POOOW!')
