#PROBLEMA 07

# Desenvolva um algoritmo e um fluxograma para um programa que permita com que o usuário insira dois números decimais.
# O programa devera então mostrar (conforme exemplo):
# A média dos números digitados.
# 
# Exemplo:
# Olá usuário, digite o número 1: 10
# Digite o número 2: 5
# Portanto, a média dos números digitados é: 7.5


#ENTRADA DE DADOS

numero1 = float(input("Olá usuário, digite o numero 1:"))
numero2 = float(input("Digite o numero 2:"))


#PROCESSAMENTO

media = (numero1 + numero2)/2

#SAÍDA DE DADOS

print("Portanto, a média dos números digitados é:", str(media))
