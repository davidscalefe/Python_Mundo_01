# Cores no Terminal

print('\33[1;32;40mOlá Mundo!\33[m')

# Style = 0- None 1- Bold 4- Underline 7- Negative
#Text = 30- Branco 31- Vermelho 32- Verde 33- Amarelo 34- Azul 35- Roxo 36- Azul Claro 37- Cinza
#Back = 40- Branco 41- Vermelho 42- Verde 43- Amarelo 44- Azul 45- Roxo 46- Azul Claro 47- Cinza

nome = 'David'
print('Olá, muito prazer em ti conhecer {}{}{}'.format('\033[4;36m',nome,'\033[m'))

# Outra Forma

nome1 = "DavidCalefe"
cores = {'limpa' : '\033[m', 'azul' : '\033[34m', 'amarelo' : '\033[33m', 'pretoebraco' : '\033[7;30m'}
print('Meu nome é {}{}{}!!'.format(cores['azul'], nome1, cores['limpa']))