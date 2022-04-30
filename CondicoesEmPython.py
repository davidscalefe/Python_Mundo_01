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