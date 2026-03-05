# Estruturas de Controle em Python

# IF / ELSE
idade = 20  # definindo a variável idade

# Se a idade for maior ou igual a 18, imprime que é maior de idade
if idade >= 18:
    print("Você é maior de idade")
# Caso contrário, imprime que é menor de idade
else:
    print("Você é menor de idade")


# FOR
# O loop for percorre uma sequência de números
# Aqui, range(1, 10) gera números de 1 até 9
for i in range(1, 10):
    print("Número:", i)


# WHILE
# O loop while repete enquanto a condição for verdadeira
cont = 1  # inicializando a variável cont

# Enquanto cont for menor ou igual a 5, o bloco será executado
while cont <= 5:
    print("Contagem:", cont)
    cont += 1  # incrementa 1 a cada repetição para não ficar infinito
