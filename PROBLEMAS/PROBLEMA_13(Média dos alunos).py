# Escreva um algoritmo e o fluxograma de um programa que permita que o usuário insira a média final da disciplina.
# De acordo com o valor digitado, o programa deve imprimir na tela as seguintes respostas:

# Média maior ou igual a 6 - Aprovado
# Média menor do que 4 - Reprovado
# Média entre 4 e 5.9 - Exame Final


#Entrada de dados

mediafinal = float(input("insira sua média final: "))

#Processamento/Saída de dados

if mediafinal >= 6:
    print("Você foi aprovado")
else:    
    if mediafinal < 4:
        print("Você foi reprovado")
    else:
        print("Exame final")
        



