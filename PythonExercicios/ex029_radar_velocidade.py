limite = float(input('Qual o limite de velocidade: '))
veloc = float(input('Qual a velocidade atual do veículo: '))

if veloc > limite:
    print(f'MULTADO! Você excedeu o limite de {limite} Km/h permitido, você está a {veloc} Km/h')
    mul = (veloc - limite) * 7
    print(f'Você deve pagar a multa de R${mul:.2f}.')

elif veloc == limite:
    print(f'Tenha atenção, está quase excedendo o limite de velocidade que é {limite:.0f}Km/h!')

else:
    print(f'Muito bem, preserve a vida!')
print('Tenha um bom dia. Dirija com segurança!')
