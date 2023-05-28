from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JÚNIOR"
elif idade <= 25:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

print(f"O atleta tem {idade} anos e sua categoria é {categoria}.")
