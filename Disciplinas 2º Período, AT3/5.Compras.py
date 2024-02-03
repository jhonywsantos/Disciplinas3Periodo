'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A. Qual é o total gasto na compra.
B. Quantos produtos custam mais de R$ 1000.
C. Qual é o nome do produto mais barato.'''

total_gasto = 0
produtos_mais_de_1000 = 0
nome_produto_mais_barato = ''
preco_produto_mais_barato = float('inf')

continuar = 'S'
while continuar == 'S':
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$ "))
    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_mais_de_1000 += 1
    if preco_produto < preco_produto_mais_barato:
        nome_produto_mais_barato = nome_produto
        preco_produto_mais_barato = preco_produto
    continuar = input("Deseja adicionar mais um produto? (S/N): ").upper()

print(f"A. Total gasto na compra: R$ {total_gasto:.2f}")
print(f"B. Produtos que custam mais de R$ 1000: {produtos_mais_de_1000}")
print(f"C. Nome do produto mais barato: {nome_produto_mais_barato}")
