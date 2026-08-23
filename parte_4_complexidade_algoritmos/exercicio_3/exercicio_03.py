# Torres de Hanoi
# Cenário. Um quebra-cabeça clássico: três pinos e discos de tamanhos diferentes, empilhados por tamanho no primeiro pino. A missão é mover a pilha inteira para o último pino, um disco de cada vez, nunca colocando um disco maior sobre um menor.
# Tarefa: Resolva as Torres de Hanoi para n discos, imprimindo a sequência de movimentos necessária.


def hanoi(n: int, origem: str, destino: str, auxiliar: str):
    # Caso base: Mover apenas 1 disco diretamente da origem para o destino
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    # Passo 1: Mover n-1 discos da origem para a haste auxiliar
    hanoi(n - 1, origem, [LACUNA_1], destino)

    # Passo 2: Mover o disco restante (disco n) para a haste destino
    print(f"Mover disco {n} de {origem} para {destino}")

    # Passo 3: Mover os n-1 discos da haste auxiliar para o destino
    [LACUNA_2]

# Exemplo de execução para 3 discos
hanoi(3, 'A', 'C', 'B')