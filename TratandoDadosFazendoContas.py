from unicodedata import name
from dataclasses import dataclass
from timeit import repeat
from tkinter import N
# TRATANDO MÓDULOS DO PYTHON

# Primeiro Desafio
print('{:=^80}'.format('Primeiro Desafio'))
print ('Ola mundo')


# Segundo Desafio
print('{:=^80}'.format('Segundo Desafio'))
nome = input('Qual seu nome: ')
print('Bem vindo {}!'.format(nome))


# Terceiro Desafio
print('{:=^80}'.format('Terceiro Desafio'))                           # TIPOS PRIMITIVOS
val1 = int(input('Digite um valor: '))                                # Int = 7, -4, 0, 9875
val2 = int(input('Digite outro valor: '))                             # Float = 4.5, 0.076, -15,223, 7.0
res = val1 + val2                                                     # Bool = True, false
print('A soma entre {} e {} e igual a {}!'.format(val1, val2, res))   # str = 'Ola', '7.5', ''


# Quarto Exercicio
print('==============================================================================')
resposta = input('Escreva alguma coisa: ')
print('O tipo primitivo desse valor e: ',type(resposta))
print('So tem espaco? ',resposta.isspace())
print('E um numero? ',resposta.isnumeric())
print('E alfabetico? ',resposta.isalpha())
print('E alfanumerico? ',resposta.isalnum())
print('Esta em maiusculas? ',resposta.isupper())
print('Esta em minusculas? ',resposta.islower())
print('Esta capitalizada? ',resposta.istitle())


# Quinto Exercicio
print('==============================================================================')                        
m = 5 * 2               # OPERADORES ARITMÉTICOS
a = 5 + 2               # + = Adição            ** = Potência
p = 5 ** 2              # - = Subtração         // = Divisão inteira
s = 5 - 2               # * = Multiplicação      % = Resto da divisão
di = 5 // 2             # / = Divisão
rd = 5 % 2
d = 5 / 2
print('Adicao           5 +  2 = ',a)
print('Potencia         5 ** 2 = ',p)
print('Subtracao        5 -  2 = ',s)
print('Divisao inteira  5 // 2 = ',di)     
print('Multiplicacao    5 *  2 = ',m)
print('Resto da divisao 5 %  2 = ',rd)
print('Divisao          5 /  2 = ',d)


# Desafio 005
print('==============================================================================')
num = int(input('Escreva um numero: '))
suc = num + 1
ant = num - 1                    # Outra forma .format(num, (num+1), (num-1))
print('O sucessor de {} e {} e o antecessor {}'.format(num, suc, ant))


# Desafio 006
print('==============================================================================')
dob = num * 2
tri = num * 3
rai = num ** (1/2)                               # Outra forma .format(num, (num*2), (num*3), (num**(1/2)))
print('O dobro de {} e {} o triplo {} e a raiz quadrada {:.2f}'.format(num, dob, tri, rai))


# Deafio 007
print('==============================================================================')
primeira_nota = int(input('Primeira nota? '))
segunda_nota = int(input('Segunda nota? '))
media = (primeira_nota + segunda_nota) / 2
if (media >= 60):
    print('Parabens voce passou! \nA media da sua nota é {}'.format(media))
else: 
    print('Voce reprovou!')


# Desafio 008
print('==============================================================================')
metros = int(input('Quantos metros? '))
centimetros = metros * 100
milimetros = metros * 1000
print('{} metros tem {} centimetros \n{} metros tem {} milimetros'.format(metros, centimetros, metros, milimetros))


# Desafio 009
print('==============================================================================')
contador = 0
tabuada = int(input('Digite um numero inteiro qualquer: '))
print('Tabuada de {}'.format(tabuada))
while (contador <=10):
    resultado = tabuada * contador
    print('{} * {} = {}'.format(tabuada, contador, resultado))
    contador = contador +1


# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos DOLARES ela pode comprar. considere US$1,00 = R$3,27
print('==============================================================================')
print('Cotacao do dolar hoje 04/04/2022: R$4,60 Real brasileiro')
carteira = float(input('Quanto de dinherio voce tem? R$'))
dolar = carteira / 4.60
print('Com R${:.2f} voce compra US${:.2f} Dolar americano'.format(carteira, dolar))

   
# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintala, sabendo que cada litro de tinta pinta uma area de 2m².
print('==============================================================================')
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
litro = area / 2
print('Sua area total e de {:.2f}² Metros'.format(area))
print('Voce vai precisar de {:.2f}Lt para pintar sua parede'.format(litro))


# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% dedesconto.
print('==============================================================================')
produto = float(input('Qual o valor do produto? R$'))
desconto = produto - (produto * 5 / 100)
print('Voce ganhou 5% de desconto')
print('Valor final do produto a ser pago R${:.2f}'.format(desconto))


# Desafio 013
# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
print('==============================================================================')
salario = float(input('Qual o seu salario? R$'))
aumento = salario + (salario * 15 / 100)
print('Vou dar 15% de aumento seu novo salario e R${:.3f}'.format(aumento))

# Desafio 014
# Escreva um programa que converta uma temperatura digitada em °C Grau Celsius para °F Fahrenheit
print('==============================================================================')
temperatura = int(input('Informe a temperatura em C: '))
grauf = temperatura * 1.8 + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(temperatura, grauf))

# Desafio 015
# Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de duas pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('==============================================================================')
km = float(input('Quantos Km percorreu? '))
dia = float(input('Quantos dias? '))
kmrodado = 0.15 * km
diapago = 60 * dia
total = kmrodado + diapago
print('Voce vai pagar R${:.2f} pelo total de Km rodado mais R${:.2f} dos {:.0f} dias que da um total de R${:.2f}'.format(kmrodado, diapago, dia, total))