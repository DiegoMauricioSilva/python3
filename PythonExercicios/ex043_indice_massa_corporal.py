peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = "Abaixo do Peso"
elif imc < 25:
    status = "Peso Ideal"
elif imc < 30:
    status = "Sobrepeso"
elif imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade Mórbida"

print(f"Seu IMC é {imc:.2f} e seu status é: {status}")
