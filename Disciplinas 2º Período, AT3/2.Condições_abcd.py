'''Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do
que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem
positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão
escrever "Valores não aceitos".'''

a = int(input('Digite um valor para "A": '))
b = int(input('Digite um valor para "B": '))
c = int(input('Digite um valor para "C": '))
d = int(input('Digite um valor para "D": '))

soma1 = a + b
soma2 = c + d
print(f'Os valores de A + B foram {soma1} e os valores de C + D foram {soma2}')

# Verifica se C e D são pares
if c % 2 == 0 and d % 2 == 0:
    if b > c and d > a:
        print('Valores Aceitos, pois B é maior que C e D é maior que A.')
    else:
        print('Valores Não Aceitos, pois B não é maior que C ou D não é maior que A.')
else:
    print('Valores Não Aceitos, pois C e D precisam ser pares.')




