# Recursão básica
# Cenário. Um sistema de loteria precisa calcular de quantas formas diferentes n números podem ser sorteados em sequência — um cálculo que depende diretamente do fatorial de n.
# Tarefa: Implemente o fatorial recursivo fatorial(n: int) -> int, tratando n < 0 com um erro apropriado (fatorial não é definido para números negativos).

def fatorial(n: int) -> int:
    # Validação para números negativos
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos")
    
    # Caso base da recursão
    if n == 0 or n == 1:
        return 1
    
    # Passo recursivo
    return n * fatorial(n - 1)

# Exemplo de uso
try:
    resultado = fatorial(5)
    print(f"5! = {resultado}")
except ValueError as e:
    print(f"Erro: {e}")