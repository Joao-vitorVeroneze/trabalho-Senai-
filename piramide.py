# verifica se é primo
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#exibe a piramide de numeros primos
def piramide_primos(N, crescente=True):
    primos = [num for num in range(2, N + 1) if eh_primo(num)]
    linhas = range(1, len(primos) + 1) if crescente else range(len(primos), 0, -1)
    
    index = 0
    for linha in linhas:
        print(" ".join(map(str, primos[index:index + linha])))
        index += linha

# solicita a numero N
try:
    N = int(input("Digite um número inteiro N: "))
    direcao = input("Deseja a pirâmide crescente? (Digite 'sim' ou 'não'): ").strip().lower()
    piramide_primos(N, crescente=(direcao == 'sim'))
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido.")
