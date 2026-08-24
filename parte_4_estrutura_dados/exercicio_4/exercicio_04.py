# Grafos (conceitual + prático)
# Cenário. Um aplicativo de mapas precisa saber, a partir da sua localização atual, quais lugares são alcançáveis e em que ordem eles seriam visitados numa busca camada por camada — a base de qualquer cálculo de rota.
# Tarefa: Descreva, em poucas frases, como grafos modelam rotas entre lugares. Em seguida, represente um grafo como dicionário de adjacência e implemente uma busca em largura (BFS).

from collections import deque

def bfs(grafo: dict, inicio: str) -> list:
    visitados = set()
    # A Fila garante a ordem de exploração por camadas (FIFO)
    fila = deque([inicio])
    visitados.add(inicio)
    ordem_visita = []

    while fila:
        # Remove o próximo vértice da fila
        vertice = fila.[LACUNA_1]()
        ordem_visita.append(vertice)

        # Explora os vizinhos diretos do vértice atual
        for vizinho in grafo[vertice]:
            if vizinho [LACUNA_2] visitados:
                visitados.add(vizinho)
                fila.[LACUNA_3](vizinho)

    return ordem_visita

# Grafo de rotas representado como Dicionário de Adjacência
mapa = {
    'Centro': ['Bairro A', 'Bairro B'],
    'Bairro A': ['Centro', 'Bairro C'],
    'Bairro B': ['Centro', 'Bairro D'],
    'Bairro C': ['Bairro A'],
    'Bairro D': ['Bairro B']
}

# Execução a partir do 'Centro'
resultado = bfs(mapa, 'Centro')
print("Ordem de visitação BFS:", resultado)