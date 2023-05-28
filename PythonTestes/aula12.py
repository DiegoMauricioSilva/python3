nome = str(input('Qual é seu nome : '))
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Aline' or nome == 'Maria' or nome == 'Mauricio':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')
