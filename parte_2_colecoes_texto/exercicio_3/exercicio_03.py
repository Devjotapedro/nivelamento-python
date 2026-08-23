# Comprehensions
# Cenário. Um professor de matemática quer uma lista rápida dos quadrados dos números pares até 20 para ilustrar um exercício na lousa, sem escrever um laço for de várias linhas.
# Tarefa: Gere uma lista com os quadrados dos números pares de 1 a 20, usando uma list comprehension.

lista_quadrados = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(lista_quadrados)