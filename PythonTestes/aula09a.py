
#len(frase): retorna o comprimento (número de caracteres) da string.
#frase.lower(): retorna uma nova string com todos os caracteres em minúsculo.
#frase.upper(): retorna uma nova string com todos os caracteres em maiúsculo.
#frase.capitalize(): retorna uma nova string com o primeiro caractere em maiúsculo e o resto em minúsculo.
#frase.replace(substring1, substring2): retorna uma nova string onde todas as ocorrências de substring1 são substituídas por substring2.
#frase.strip(): retorna uma nova string sem os espaços em branco no início e no final.
#frase.split(separador): retorna uma lista de substrings separados pelo separador.
#frase.startswith(substring): retorna True se a string começa com a substring.
#frase.endswith(substring): retorna True se a string termina com a substring.
#frase.count(substring): retorna o número de ocorrências da substring na string.
#frase.capitalize(): retorna uma nova string com o primeiro caractere em maiúsculo e o restante em minúsculo.
#frase.count(substring): retorna o número de ocorrências da substring na string


frase = ('Curso em Video Python')
print(frase[::2])
print(frase.upper().count('O'))
