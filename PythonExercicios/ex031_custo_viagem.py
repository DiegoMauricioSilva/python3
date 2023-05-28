dist = float(input('Digite a distância da sua viagem: '))

if dist >= 100:
    vlr = dist * 0.45
    print(f'Você está prestes a realizar uma viagem de {dist:.0f}Km, leve travesseiro!')
    print(f'E o preço de sua passagem será de R${vlr:.2f}')

elif dist < 100:
    vlr = dist * 0.5
    print(f'Você está prestes a realizar uma viagem de {dist}Km, tenha uma excelente viagem!')
    print(f'E o preço de sua passagem será de R${vlr:.2f}')

elif dist < 50:
    vlr = dist * 0.4
    print(f'Você está prestes a realizar uma viagem de {dist}Km, relaxe, vai ser rápido!')
    print(f'E o preço de sua passagem será de R${vlr:.2f}.')
