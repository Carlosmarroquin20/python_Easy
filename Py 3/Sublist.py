lista_de_listas = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]

# Filtrar sublistas que tienen más de 2 elementos
filtrada = [sublista for sublista in lista_de_listas if len(sublista) > 2]

print(filtrada)  # Imprimirá: [[3, 4, 5], [7, 8, 9, 10]]
