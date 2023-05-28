from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade < 18:
    tempo_restante = 18 - idade
    print(f"Você ainda vai se alistar ao serviço militar. Faltam {tempo_restante} ano(s) para o alistamento.")
elif idade == 18:
    print("É hora de se alistar ao serviço militar!")
else:
    tempo_passado = idade - 18
    print(f"Já passou do tempo de se alistar ao serviço militar. Passaram-se {tempo_passado} ano(s) do prazo.")
