'''Faça um programa que, dado um número n (1 <= n <= 40) printa na tela os números de 1 até o número da iteração atual, 
sendo que serão feitas n iterações,'''

interações = int(input("Digite o valor de um número que você deseja visualizar as interações: "))
for i in range(1, interações + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

