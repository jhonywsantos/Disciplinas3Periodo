'''Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por 
um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.'''

dias = int(input('Digite a quantidade de dias que o veículo ficou sob sua posse:'))
quilometragem = float(input('Informe a quantidade da quilometragem rodada: '))

valor_diaria = 90.00
quilometragem_inclusa = 100
taxa_excesso = 12.00

valor_total = (dias * valor_diaria) + max(0, quilometragem - (dias * quilometragem_inclusa)) * taxa_excesso

print(f"O valor total a ser pago pelo cliente é equivalente a: R$ {valor_total:.2f}")