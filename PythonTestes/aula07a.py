n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f} '.format(s, m, d))
print('Divisão inteira {}, e potência {}'.format(di, e))
#Para não quebrar a linha faça como abaixo
print('A soma é {}, o produto é {} e a divisão é {:.3f} '.format(s, m, d), end=' ')
print('Divisão inteira {}, e potência {}'.format(di, e))
#Para quebrar linha no meio da mesma, digite \n
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f} '.format(s, m, d))
print('Divisão inteira {}, e potência {}'.format(di, e))
