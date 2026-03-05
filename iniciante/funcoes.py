# Funções em Python

# Função simples sem parâmetros
# Essa função apenas imprime uma saudação quando chamada
def saudacao():
    print("Olá, tudo bem?")

# Chamando a função
saudacao()


# Função com parâmetros
# Essa função recebe dois valores (x e y) e retorna a soma deles
def soma(x, y):
    return x + y

# Chamando a função e armazenando o resultado
resultado = soma(6, 10)
print("Resultado da soma:", resultado)


# Função com parâmetro padrão
# Se nenhum nome for passado, o valor padrão será "João"
def apresentarnome(nome="João"):
    print("Meu nome é:", nome)

# Chamando a função sem passar argumento → usa o valor padrão
apresentarnome()

# Chamando a função passando um argumento → usa o valor fornecido
apresentarnome("Vitor")
