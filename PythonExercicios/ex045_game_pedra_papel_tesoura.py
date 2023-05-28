import random

print("Bem-vindo(a) ao Jokenpô (Melhor de 3)!\n")

opcoes = ["Pedra", "Papel", "Tesoura"]
placar_jogador = 0
placar_computador = 0

while placar_jogador < 2 and placar_computador < 2:
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    escolha_usuario = int(input("Digite o número da sua escolha: "))

    if escolha_usuario < 1 or escolha_usuario > 3:
        print("Escolha inválida. Por favor, digite uma opção válida.\n")
        continue

    escolha_computador = random.randint(1, 3)

    print(f"\nVocê escolheu: {opcoes[escolha_usuario - 1]}")
    print(f"O computador escolheu: {opcoes[escolha_computador - 1]}\n")

    if (
        (escolha_usuario == 1 and escolha_computador == 3)
        or (escolha_usuario == 2 and escolha_computador == 1)
        or (escolha_usuario == 3 and escolha_computador == 2)
    ):
        print("Você venceu essa rodada!\n")
        placar_jogador += 1
    elif (
        (escolha_usuario == 1 and escolha_computador == 2)
        or (escolha_usuario == 2 and escolha_computador == 3)
        or (escolha_usuario == 3 and escolha_computador == 1)
    ):
        print("O computador venceu essa rodada!\n")
        placar_computador += 1
    else:
        print("Essa rodada empatou! Vamos jogar novamente.\n")

if placar_jogador > placar_computador:
    print("Parabéns! Você venceu o jogo!")
else:
    print("O computador venceu o jogo!")

print(f"Placar Final: Jogador {placar_jogador} x {placar_computador} Computador")
