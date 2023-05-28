nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 5.0:
    print("Média abaixo de 5.0: REPROVADO")
elif media >= 5.0 and media < 7.0:
    print("Média entre 5.0 e 6.9: RECUPERAÇÃO")
else:
    print("Média 7.0 ou superior: APROVADO")
