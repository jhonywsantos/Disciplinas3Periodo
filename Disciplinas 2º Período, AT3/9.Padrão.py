
N = int(input("Digite um número inteiro N: "))

for i in range(1, N + 1):
    print(f"{i} {i * i} {i * i * i}")

for i in range(1, N + 1):
    print(f"{i} {i * i + N} {i * i * i + N}")


