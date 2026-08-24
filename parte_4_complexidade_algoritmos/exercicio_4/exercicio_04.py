# Recursão e soma
# Cenário. Um relatório de vendas chega em um formato aninhado: cada região é uma lista que pode conter tanto números de vendas quanto sublistas de sub-regiões. Somar tudo exige descer por essa estrutura sem saber, de antemão, quantos níveis de aninhamento existem.
# Tarefa: Implemente uma função recursiva que some todos os números em uma lista, mesmo quando ela contém sublistas aninhadas em qualquer profundidade.

def somar_aninhado(lista: list) -> int:
    soma_total = 0
    for elemento in lista:
        if isinstance(elemento, list):
            # Se o elemento for uma sublista, faz a chamada recursiva
            soma_total += [LACUNA_1](elemento)
        elif isinstance(elemento, (int, float)):
            # Se for um número, adiciona diretamente à soma
            soma_total += [LACUNA_2]
            
    return soma_total

# Exemplo de uso com múltiplos níveis de aninhamento
vendas = [100, [200, 300], [50, [20, 30]]]
print(f"Total de vendas: R$ {somar_aninhado(vendas)}")