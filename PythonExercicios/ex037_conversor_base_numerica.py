numero = int(input("Digite um número inteiro: "))
opcao = int(input("Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n"))

if opcao == 1:
    resultado = bin(numero)
    print(f"O número {numero} em binário é: {resultado}")
elif opcao == 2:
    resultado = oct(numero)
    print(f"O número {numero} em octal é: {resultado}")
elif opcao == 3:
    resultado = hex(numero)
    print(f"O número {numero} em hexadecimal é: {resultado}")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")
