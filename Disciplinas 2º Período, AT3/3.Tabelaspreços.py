'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10
caixas. Você foi contratado para desenvolver o programa que monta esta tabela de preços, 
que conterá os preços de 1 até 50 produtos,'''

print("*****************************************")
print("Lojas Quase Dois - Tabela de preços")
print("*****************************************")

precos = [i * 1.99 for i in range(1, 51)]
total_compra = 0
continuar_compra = True

while continuar_compra:
    numero_item = int(input("Digite o número do item (1 a 50, ou -1 para encerrar): "))
    if 1 <= numero_item <= 50:
        quantidade = int(input(f"Digite a quantidade de itens {numero_item}: "))
        total_compra += quantidade * precos[numero_item - 1]
    elif numero_item == -1:
        continuar_compra = False
    else:
        print("Número de item inválido. Por favor, digite um número entre 1 e 50.")

print(f"Total gasto: R$ {total_compra:.2f}")

