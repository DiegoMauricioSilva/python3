from random import randint
from time import sleep

computador = randint(0,5) #computador "PENSA UM NÚMERO"

print('-=-' * 25)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar o número!')
print('-=-' * 25)

jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if computador == jogador:
    print(f'Parabéns! Você venceu! O número {jogador} escolhido por você é o mesmo {computador} \n'
          f'escolhido pelo computador')

else:
    print(f'Você perdeu! O número {computador} escolhido pelo computador é diferente de seu número {jogador},\n'
          f'tente novamente!')
