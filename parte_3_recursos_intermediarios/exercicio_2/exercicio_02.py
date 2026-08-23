# Generators
# Cenário. Um painel precisa plotar pares número/quadrado sob demanda, sem montar a lista inteira de antemão — cada ponto é consumido um de cada vez, conforme o gráfico é desenhado.

# Tarefa: Implemente um generator que produza pares (n, n*n) para n de 1 a 10, e consuma os valores chamando next() manualmente.

def gerador_quadrados(limite: int):
    for n in range(1, limite + 1):
        yield(n, n*n)
        

# Instanciando o generator
meu_gerador = gerador_quadrados(10)

# Consumindo os dois primeiros valores manualmente
primeiro_ponto = next(meu_gerador)
segundo_ponto = next(meu_gerador)

print(f"Ponto 1: {primeiro_ponto}")
print(f"Ponto 2: {segundo_ponto}")