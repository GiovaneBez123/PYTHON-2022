#PROBLEMA 01 -
# Desenvolva um algoritmo e um fluxograma de um programa que permita que o usuário insira dois valores.
# O programa entao imprime a soma desses valores.


# valor1 = input("digite o valor1:")
# valor1 = float(valor1)

#ENTRADA DE DADOS
valor1 = float(input("digite o valor1: "))
valor2 = float(input("digite o valor2: "))

#PROCESSAMENTO
soma = valor1 + valor2

#SAÍDA DE DADOS
mensagem = "A soma dos valores e:\n"+ str(soma) # o soma dos valores é string e a soma é float, por isso que convertemos a soma para string.
print(mensagem)



