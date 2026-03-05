# Funções em Python

# Função simples sem parâmetros
def saudacao():
    print("Olá, tudo bem?")

saudacao()


# Função com parâmetros
def soma(x, y):
    return x + y

resultado = soma(6, 10)
print("Resultado da soma:", resultado)


# Função com parâmetro padrão
def apresentarnome(nome="João"):
    print("Meu nome é:", nome)

apresentarnome()          # usa valor padrão
apresentarnome("Vitor")   # usa valor passado
