# Biblioteca math - Funções Matematicas
# ceil - Arrendondamento para cima
# floor - Arrendondamento para baixo
# trunc - Elimina da vircula para frente
# pow (potencia) - semelhante aos dois **
# sqrt - Calcular raiz quadrada
# factorial - Calculos fatorial

# AULA 008
import emoji
print('==============================================================================')
print(emoji.emojize('Ola, Mundo :earth_americas:', use_aliases=True))

# Desafio 016
# Crie um programa que leiaum numero real quelquer pelo teclado e mostre na tela a sua porçao inteira.
from math import trunc
numeroqualquer = float(input('Digite um numero: '))
inteiro = trunc(numeroqualquer)
print('O numero {} tem a parte inteira {}'.format(numeroqualquer, inteiro))

# Desafio 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa.
print('==============================================================================')
from math import hypot
oposto = float(input('Qual o comprimento do Cateto Oposto? '))
adjacente = float(input('Qual o comprimento do cateto Adjacente? '))
hipotenusa = hypot(oposto, adjacente)
print('O valor da Hipotenusa e {:.1f}'.format(hipotenusa))

# Desafio 018
# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
print('==============================================================================')
from math import tan, sin, cos, radians
angulo = float(input('Qual o angulo? '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Seno {:.2f}, Cosseno {:.2f}, Tangente {:.2f}'.format(seno, cosseno, tangente))

# Desafio 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um program que ajude ele, lendo o nome deles e escreva o nome do escolhido.
print('==============================================================================')
from random import choice
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto Aluno: '))
sorteio = (aluno1, aluno2, aluno3, aluno4)
print('O Aluno escolhido foi {}'.format(choice(sorteio)))

# Desafio 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print('==============================================================================')
from random import shuffle
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto Aluno: '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
shuffle(sorteio)
print('Ordem de apresentacao sera:')
print(sorteio)

# Desafio 021
# Faça um prgrama em Python que abra e reproduza o audio de arquivo MP3
print('==============================================================================')
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

# Desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
print('==============================================================================')
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome com todas as letras maiúscula: {}'.format(nome.upper()))
print('Em minúscula: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
primeiro = nome.split()
print('Seu primerio nome tem {} letras'.format(len(primeiro[0])))

# Desafio 023
# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
print('==============================================================================')
numeroqualquer = int(input('Digite um numero de 0 a 9999: '))
u = numeroqualquer // 1 % 10
d = numeroqualquer // 10 % 10
c = numeroqualquer // 100 % 10
m = numeroqualquer // 1000 % 10
print('Analisando o numero {}'.format(numeroqualquer))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

# Desafio 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO.
print('==============================================================================')
cidade = str(input('Digite um nome de cidade: ')).strip()
print(cidade[:5].lower() == 'santo')

# Desafio 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"
print('==============================================================================')
nomesilva = str(input('Qual e seu nome completo? '))
nomesilva = nomesilva.lower().strip().split()
print('Seu nome tem silva? {}'.format('silva' in nomesilva))

# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a ultima vez.
frase = str(input('Escreva uma frase: ')).strip().lower()
print('Sua frase tem {} letras A'.format(frase.count('a')))
print('Primeira posicao da letra A: {}'.format(frase.find('a')+1))
print('Ultima posicao da letra A: {}'.format(frase.rfind('a')+1))

# Desafio 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
nomecomp = str(input('Digite seu nome completo: ')).strip()
divi = nomecomp.split()
print('Seu primeiro nome e: {}'.format(divi[0]))
print('Seu ultimo nome e: {}'.format(divi[len(divi)-1]))