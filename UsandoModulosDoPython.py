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
