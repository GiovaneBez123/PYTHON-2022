#PROBLEMA 02
# Desenvolva um algoritmo e um fluxograma de um programa que permita com que o usuário insira um valor representando o raio de um círculo.
# O programa deverá calcular o diâmetro  (multiplicando o raio por 2) e então calcula o comprimento da circunferência (multiplicando o diâmetro por 3,14).
# O programa deve imprimir na tela tanto o diâmetro quanto o comprimento da circunferência.

#ENTRADA DE DADOS
from tkinter import N


raio = float(input("digite o valor do raio: "))

#PROCESSAMENTO DE DADOS
diametro = raio*2
comprimento = diametro *3.14

#SAÍDA DE DADOS

print ("O valor do diametro é:",diametro, " e o valor da circunferência é:",comprimento)