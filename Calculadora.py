num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == '+':
    print(num1 + num2)
elif operador == '-':
    print(num1 - num2)
elif operador == '*':
    print(num1 * num2)
elif operador == '/':
    if num2 == 0:
        print("Erro: divisão por zero!")
    else:
        print(num1 / num2)
else:
    print("Operador inválido!")
