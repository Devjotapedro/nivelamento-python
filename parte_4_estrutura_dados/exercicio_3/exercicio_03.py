# Lista ligada
# Cenário. Um app de streaming mantém o histórico de músicas tocadas: é fácil adicionar uma música no início (a mais recente) ou no fim (a mais antiga), remover uma música específica do meio do histórico e saber, a qualquer momento, quantas músicas já foram tocadas.
# Tarefa: Implemente uma lista ligada simples com os métodos inserir_inicio, inserir_fim, remover(valor) e __len__.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self._tamanho += 1

    def inserir_fim(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = [LACUNA_1]
        self._tamanho += 1

    def remover(self, valor) -> bool:
        if self.cabeca is None:
            return False

        # Caso especial: remoção do primeiro nó
        if self.cabeca.valor == valor:
            self.cabeca = [LACUNA_2]
            self._tamanho -= 1
            return True

        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.valor != valor:
            atual = atual.proximo

        if atual.proximo is not None:
            # Desconecta o nó a ser removido pulando para o seguinte
            atual.proximo = [LACUNA_3]
            self._tamanho -= 1
            return True

        return False

    def __len__(self) -> int:
        return [LACUNA_4]