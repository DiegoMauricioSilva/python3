#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
nome = input('Digite seu nome: ')
v_carro = float(input('Digite o valor da diaria do veiculo alugado: R$'))
q_dias = int(input('Digite a quantidade de dias de locação: '))
v_km = float(input('Digite o valor do quilometro rodado: R$'))
km_p = float(input('Digite a quantidade de quilometros percorridos: '))
total = (v_carro * q_dias) + (v_km * km_p)
print(f'Senhor(a) {nome}, você deve pagar pelo veiculo o valor de R${total}')
