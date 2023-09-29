def adição(a, b):
    return a + b

def subtração(a, b):
    return a - b

def divisão(a, b):
    if b == 0:
        print("Erro: Divisão por zero não é permitida.")
        return None
    return a / b

def multiplicação(a, b):
    return a * b

def calc():
    print("Calculadora em Python\n")
    print("Digite 1, 2, 3 ou 4")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")

    escolha = input("Escolha uma operação: ")

    while escolha not in ['1', '2', '3', '4']:
        print("Resposta inválida")
        escolha = input("Escolha uma operação: ")

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = adição(n1, n2)
    elif escolha == '2':
        resultado = subtração(n1, n2)
    elif escolha == '3':
        resultado = divisão(n1, n2)
        if resultado is not None:
            print("Resultado:", resultado)
    else:
        resultado = multiplicação(n1, n2)



calc()
