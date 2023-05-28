preco = float(input("Digite o preço do produto: R$ "))
forma_pagamento = int(input("Selecione a forma de pagamento:\n"
                            "1 - À vista dinheiro/cheque\n"
                            "2 - À vista no cartão\n"
                            "3 - Em até 2x no cartão\n"
                            "4 - 3x ou mais no cartão\n"
                            "Opção: "))

if forma_pagamento == 1:
    valor_final = preco - (preco * 0.1)  # 10% de desconto
elif forma_pagamento == 2:
    valor_final = preco - (preco * 0.05)  # 5% de desconto
elif forma_pagamento == 3:
    valor_final = preco
    parcelas = valor_final / 2
    print(f"Pagamento em 2x de R$ {parcelas:.2f} (Preço normal)")
elif forma_pagamento == 4:
    valor_final = preco + (preco * 0.2)  # 20% de juros
    num_parcelas = int(input("Digite o número de parcelas desejadas: "))
    parcelas = valor_final / num_parcelas
    print(f"Pagamento em {num_parcelas}x de R$ {parcelas:.2f} (Com juros de 20%)")
else:
    print("Opção inválida. Por favor, selecione uma opção válida.")

if forma_pagamento in [1, 2]:
    print(f"Valor a ser pago: R$ {valor_final:.2f}")
