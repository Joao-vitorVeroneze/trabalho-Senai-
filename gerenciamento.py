# Definindo os conjuntos de clientes
clientes_A = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}
clientes_B = {"Carlos", "Eduardo", "Fernando", "Gabriela", "Helena"}

#A. Identificar os clientes que estão em ambos os conjuntos (interseção)
clientes_em_ambos = clientes_A & clientes_B
print("Clientes em ambos os conjuntos:", clientes_em_ambos)

#B. Identificar os clientes que estão apenas em clientes_A (diferença)
clientes_apenas_A = clientes_A - clientes_B
print("Clientes apenas em clientes_A:", clientes_apenas_A)

#C. Identificar os clientes que estão em apenas um dos conjuntos (diferença simétrica)
clientes_apenas_um_conjunto = clientes_A ^ clientes_B
print("Clientes em apenas um dos conjuntos:", clientes_apenas_um_conjunto)

#D. Calcular a porcentagem de clientes únicos
todos_clientes = clientes_A | clientes_B
clientes_unicos = len(todos_clientes)
clientes_unicos_percentual = (clientes_unicos / len(todos_clientes)) * 100
print(f"Porcentagem de clientes únicos: {clientes_unicos_percentual:.2f}%")
