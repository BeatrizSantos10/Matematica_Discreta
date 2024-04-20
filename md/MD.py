def ex1():
    conjunto_a = {1, 2, 3, 4}
    conjunto_b = {3, 4, 5, 6}

    print("Conjunto A:", conjunto_a)
    print("Conjunto B:", conjunto_b)

    uniao = conjunto_a.union(conjunto_b)
    print("União:", uniao)

    intersecao = conjunto_a.intersection(conjunto_b)
    print("Interseção:", intersecao)

    diferenca = conjunto_a.difference(conjunto_b)
    print("Diferença A - B:", diferenca)

    subconjunto = conjunto_b.issubset(conjunto_a)
    print("Conjunto B é subconjunto de A:", subconjunto)


def ex2():
    p = input("Digite o valor de verdade para P (True/False): ").lower() == 'true'
    q = input("Digite o valor de verdade para Q (True/False): ").lower() == 'true'

    while True:
        print("Escolha a operação lógica:")
        print("1. Negação (~)")
        print("2. Conjunção (˄)")
        print("3. Disjunção (˅)")
        print("4. Condicional (→)")
        print("5. Bicondicional (↔)")

        escolha = input("-> ")

        if escolha in ['1', '~']:
            print("Negação de P:", not p)
            print("Negação de Q:", not q)
            break
        elif escolha in ['2', '˄']:
            print("Conjunção de P e Q:", p and q)
            break
        elif escolha in ['3', '˅']:
            print("Disjunção de P e Q:", p or q)
            break
        elif escolha in ['4', '→']:
            print("Condicional de P para Q:", not p or q)
            break
        elif escolha in ['5', '↔']:
            print("Bicondicional de P para Q:", p == q)
            break
        else:
            print("Opção inválida. Escolha novamente.")


def ex3():
    numero = int(input("Digite um número inteiro positivo: "))

    if verificar_primo(numero):
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")


def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def ex4():
    x = float(input("Digite um valor para x: "))
    resultado = calcular_funcao(x)
    print("O resultado da função f(x) = x^2 + 3x - 7 é:", resultado)


def calcular_funcao(x):
    return x ** 2 + 3 * x - 7


def ex5():
    numero = int(input("Digite um número inteiro para verificar a paridade: "))

    if verificar_paridade(numero):
        print("O número", numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")


def verificar_paridade(numero):
    return numero % 2 == 0


if __name__ == "__main__":
    while True:
        print("\n\nEscolha um exercício para executar:")
        print("1. Conjunto")
        print("2. Lógicas")
        print("3. Primos")
        print("4. Função")
        print("5. Paridade")
        print("0. Sair")
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
