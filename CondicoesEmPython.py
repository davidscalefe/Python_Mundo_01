# Desafio 028
# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.
# O programa devera escrever na tela se o usuario venceu ou perdeu.
print('==============================================================================')
import random
pensar = [0, 1, 2, 3, 4, 5]
nescolhido = int(input('Digite um numero de 0 a 5: '))
print('Vamos ver se voce acertou!')
sorteio = random.choice(pensar)
if nescolhido == sorteio:
    print('VOCE ACERTOU \nPARABENS!')
else:
    print('VOCE ERROU! \nTente novamente!')
    
# Desafio 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
print('==============================================================================')
limite = 80
velocidade = int(input('Qual foi a velocidade: '))
acima = velocidade - limite
if velocidade > 80:
    print('Voce foi multado! \nValor da multa R${}'.format(7 * acima))
elif velocidade == 80:
    print('Voce esta no limite da velocidade ATENCAO')
elif velocidade < 40:
    print('Voce esta devagar em uma via de 80km!')
else:
    print('Parabens voce esta na velocidade correta!')

# Desafio 030 
# Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou IMPAR.
print('==============================================================================')
parimpar = int(input('Digite um numero: '))
r = parimpar % 2
if r == 0:
    print('Par')
else:
    print('Impar')

# Desafio 031
# Desenvolva um programa que pergunte a distacia de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 para viagens mais longas.
print('==============================================================================')
distancia = int(input('Qual a distancia da viagem em km? '))
curta = 0.50
longa = 0.45
if distancia <= 200:
    print('Valor da Passagem: R${}'.format(curta * distancia))
else:
    print('Valor da Passagem: R${}'.format(longa * distancia))

# Desafio 032
# Faça um program que leia um ano qualquer e mostre se ele é BISSEXTO.
print('==============================================================================')
ano = int(input('Digite um ano qualquer: '))
bi = ano % 4
if bi == 0:
    print('Ano bissexto')
else:
    print('Nao e bissexto')


# Desafio 033
# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
print('==============================================================================')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O numero maior e {}'.format(maior))
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O menor numero e {}'.format(menor))

# Desafio 034
# Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
print('==============================================================================')
salario = float(input('Qual o seu salario? '))
base = 1250
if salario > base:
    print('Voce ganhou 10% de aumento, seu novo salario R${}'.format(salario + (salario * 10 / 100)))
else:
    print('Voce ganhou 15% de aumento, seu novo salario R${}'.format(salario + (salario * 15 / 100)))
# Desafio 035
# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.
print('==============================================================================')
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo') 