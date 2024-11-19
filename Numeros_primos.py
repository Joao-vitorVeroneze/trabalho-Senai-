N = int(input("Digite um número inteiro N: "))
print(f"Números primos entre 1 e {N}:")

'''de 2 ate o numero digitado'''
for num in range(2, N + 1):
    '''verifica se é primo'''
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(num, end=" ")
