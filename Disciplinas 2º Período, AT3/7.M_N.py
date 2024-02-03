'''Seu objetivo é determinar o maior múltiplo de um inteiro dado menor do que ou igual a
um outro inteiro dado. A saída consiste do maior número que seja múltiplo de M e menor
ou igual a N, se não houver um múltiplo de M menor ou igual a N você deve imprimir
"sem múltiplos menores que N", onde N deve ser substituído pelo valorde entrada N.'''
 
M = int(input("Digite o valor de M: "))
N = int(input("Digite o valor de N: "))

maior_multiplo = 0

for i in range(N, 0, -1):
    if i % M == 0 and maior_multiplo == 0:
        maior_multiplo = i

if maior_multiplo > 0:
    print(maior_multiplo)
else:
    print(f"sem múltiplos menores que {N}")
