# Pilha
# Cenário. Um editor de texto simples precisa de uma função “desfazer”: a última ação feita é sempre a primeira a ser desfeita. Antes de implementar o editor inteiro, vale testar a estrutura de dados por trás dele com algo simples: inverter uma string, caractere por caractere.
# Tarefa: Implemente uma classe Pilha com push, pop, top e is_empty. Use-a para inverter uma string.

class Pilha:
    def __init__(self):
        self._itens = []

    def push(self, item):
        self._itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self._itens.[LACUNA_1]()
        raise IndexError("A pilha está vazia")

    def top(self):
        if not self.is_empty():
            return self._itens[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._itens) == 0


def inverter_string(texto: str) -> str:
    pilha = Pilha()
    
    # Empilha todos os caracteres da string
    for caractere in texto:
        pilha.[LACUNA_2](caractere)

    texto_invertido = ""
    # Desempilha construindo a nova string
    while not pilha.is_empty():
        texto_invertido += pilha.pop()

    return texto_invertido

# Exemplo de uso
original = "CodeQuest"
invertido = inverter_string(original)
print(f"Original: {original} | Invertido: {invertido}")