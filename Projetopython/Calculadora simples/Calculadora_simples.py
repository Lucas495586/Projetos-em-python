def calculadora():
    a = int(input("Escolha o primeiro número: "))
    b = int(input("Escolha o segundo número: "))

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b

    print("Qual operação você quer?")
    escolha = int(input("1 - soma; 2 - subtração; 3 - multiplicação; 4 - divisão: "))

    if escolha == 1:
        print("Resultado da soma:", soma)
    elif escolha == 2:
        print("Resultado da subtração:", subtracao)
    elif escolha == 3:
        print("Resultado da multiplicação:", multiplicacao)
    elif escolha == 4:
        if b != 0:
            print("Resultado da divisão:", divisao)
        else:
            print("Erro: divisão por zero.")
    else:
        print("Escolha inválida.")

calculadora()
   
