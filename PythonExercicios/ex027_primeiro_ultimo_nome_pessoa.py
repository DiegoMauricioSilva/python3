n = str(input('Qual seu nome completo: ')).strip()
nome = n.split()
print('Olá {}, satisfação em te conhecer!'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))
