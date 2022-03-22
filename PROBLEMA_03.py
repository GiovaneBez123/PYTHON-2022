#PROBLEMA 03 -
#Desenvolva um algoritmo e um fluxograma para um programa que permita com que o usuário insira o nome, o sobrenome e a idade.

#ENTRADA DE DADOS

nome = input("digite seu nome:\n")
sobrenome = input("digite seu sobrenome:\n")
idade = input("digite sua idade:\n")

#PROCESSAMENTO

mensagem = "olá " + nome + " " + sobrenome + ",\n"
mensagem = mensagem + "sua idade é de " + idade + " anos."


#SAIDA DE DADOS

print(mensagem)
