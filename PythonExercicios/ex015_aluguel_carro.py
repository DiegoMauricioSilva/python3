nome = input('Digite seu nome: ')
valor_diaria = float(input('Digite o valor da diária do veículo alugado: R$ '))
valor_km = float(input('Digite o valor do quilômetro rodado: R$ '))
km_percorridos = float(input('Digite a quantidade de quilômetros percorridos: '))
dias_locacao = int(input('Digite a quantidade de dias de locação: '))
valor_aluguel = (valor_diaria * dias_locacao) + (valor_km * km_percorridos)

print(f'Senhor(a) {nome}, você deve pagar pelo veículo o valor de R${valor_aluguel:.2f}')
