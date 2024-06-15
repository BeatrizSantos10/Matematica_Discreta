def main():
    while True:
        print("\n\nEscolha um exercício para executar:")
        print("|1. Endorrelação")
        print("|2. Fatorial")
        print("|3. Fecho transitivo")
        print("|4. Fibonacci")
        print("|5. Permutações")
        print("|0. Sair|")
        choice = input("-> ")

        if choice == '1':
            ex1()
        elif choice == '2':
            ex2()
        elif choice == '3':
            ex3()
        elif choice == '4':
            ex4()
        elif choice == '5':
            ex5()
        elif choice == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

# Endorrelação
def ex1():
    relacao = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)}
    verifica_propriedades(relacao)

def verifica_propriedades(relacao):
    simetrica = True
    antissimetrica = True
    reflexiva = True
    irreflexiva = True
    transitiva = True

    elementos = {x for par in relacao for x in par}

    for (a, b) in relacao:
        if a != b and (b, a) not in relacao:
            simetrica = False
        if a != b and (b, a) in relacao:
            antissimetrica = False

    for e in elementos:
        if (e, e) not in relacao:
            reflexiva = False
        if (e, e) in relacao:
            irreflexiva = False

    for (a, b) in relacao:
        for (c, d) in relacao:
            if b == c and (a, d) not in relacao:
                transitiva = False

    print(f"Simétrica: {simetrica}")
    print(f"Antissimétrica: {antissimetrica}")
    print(f"Reflexiva: {reflexiva}")
    print(f"Irreflexiva: {irreflexiva}")
    print(f"Transitiva: {transitiva}")

# Fatorial
def ex2():
    numero = int(input("Digite um número para calcular o fatorial: "))
    fatorial = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {fatorial}")

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Fecho transitivo
def ex3():
    matriz_adjacencia = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    calcular_fecho_transitivo(matriz_adjacencia)

def calcular_fecho_transitivo(matriz):
    tamanho = len(matriz)
    fecho_transitivo = [linha[:] for linha in matriz]

    for k in range(tamanho):
        for i in range(tamanho):
            for j in range(tamanho):
                fecho_transitivo[i][j] = fecho_transitivo[i][j] or (fecho_transitivo[i][k] and fecho_transitivo[k][j])

    print("Fecho Transitivo:")
    for linha in fecho_transitivo:
        print(" ".join(map(str, linha)))

# Fibonacci
def ex4():
    quantidade_termos = int(input("Digite a quantidade de termos da sequência Fibonacci: "))
    print(f"Sequência Fibonacci até o {quantidade_termos}º termo:")
    for i in range(quantidade_termos):
        print(calcular_fibonacci(i), end=" ")

def calcular_fibonacci(n):
    if n <= 1:
        return n
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        anterior, atual = atual, anterior + atual
    return atual

# Permutações
def ex5():
    elementos = [1, 2, 3]
    permutacoes = gerar_permutacoes(elementos)
    print("Todas as permutações:")
    for permutacao in permutacoes:
        print(permutacao)

def gerar_permutacoes(elementos):
    return list(itertools.permutations(elementos))

if __name__ == "__main__":
    main()
