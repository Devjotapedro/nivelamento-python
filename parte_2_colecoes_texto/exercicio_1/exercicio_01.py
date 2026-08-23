# Listas e operações
# Cenário. Você está fazendo compras no mercado e quer controlar a lista pelo celular: adicionar itens que lembrar no caminho, remover os que já foram para o carrinho e corrigir a quantidade de algo digitado errado.
# Tarefa: Implemente uma lista de compras (uma list de itens) que permita adicionar, remover e atualizar itens. Ao final, mostre o total de itens e a lista ordenada.

lista_compras = ["massa", "leite", "ovos", "pão"]

#adicionar
lista_compras.append("treloso")
print(lista_compras)

#remove
lista_compras.remove("leite")
print(lista_compras)

#atualizar
lista_compras[0] = "massa de bolo"
print(lista_compras)

#ordenar
lista_compras.sort()
print(lista_compras)