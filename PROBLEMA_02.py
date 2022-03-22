#PROBLEMA 02 -
# Desenvolva um algoritmo e um fluxograma de um programa que permita com que o usuário insira um valor representando o raio de um círculo.
# O programa deverá calcular o diâmetro  (multiplicando o raio por 2) e então calcula o comprimento da circunferência (multiplicando o diâmetro por 3,14).
# O programa deve imprimir na tela tanto o diâmetro quanto o comprimento da circunferência.

#ENTRADA DE DADOS

raio = float(input("Digite o valor de raio:"))

#PROCESSAMENTO
PI = 3.14
diametro = raio * 2
comprimento = diametro * PI

#SAIDA DE DADOS
print("diametro:",diametro,"\n","comprimento:",comprimento)

