
# Listas são coleções de valores que podem ser alteradas.

# Criando uma lista de marcas de carros
marcas = ["Porsche", "BMW", "Mercedes", "McLaren"]

# Mostrando a lista completa
print("Lista inicial:", marcas)

# Acessando elementos pelo índice
# Lembre-se: o índice começa em 0 → Porsche é [0], BMW é [1]
print("Primeira marca (índice 1):", marcas[1])

# Adicionando um item na lista
marcas.append("BYD")
print("Depois de adicionar:", marcas)

# Removendo um item da lista
marcas.remove("BYD")
print("Depois de remover:", marcas)

# Percorrendo a lista com um laço for
print("Percorrendo a lista:")
for marca in marcas:
    print("Marca:", marca)

# Também dá para percorrer usando índices
print("Percorrendo com índices:")
for i in range(len(marcas)):
    print(f"Índice {i} → {marcas[i]}")
