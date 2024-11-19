print("ola responda as seguintes perguntas:")

nome = input ("qual seu nome ? ")
idade = float(input ("qual sua idade ? "))
peso = float(input ("qual seu peso ? "))
altura = float(input ("qual sua altura? "))



imc = peso / (altura * 2) 

print (f"{nome} com {idade} anos tem um IMC de {imc}")