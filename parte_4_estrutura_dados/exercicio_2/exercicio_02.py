# Fila
# Cenário. Uma impressora compartilhada do laboratório recebe vários documentos ao longo do dia e imprime na ordem de chegada: o primeiro documento enviado é o primeiro a sair, mesmo que outros cheguem enquanto ele ainda está sendo processado.
# Tarefa: Implemente uma fila usando collections.deque e simule uma fila de impressão, em que cada documento tem nome e paginas.

from collections import deque

class FilaImpressao:
    def __init__(self):
        # Utiliza deque para otimizar remoções e inserções nas extremidades
        self._documentos = deque()

    def adicionar_documento(self, nome: str, paginas: int):
        # Adiciona um novo documento ao final da fila
        self._documentos.[LACUNA_1]({"nome": nome, "paginas": paginas})

    def processar_proximo(self):
        # Remove e retorna o primeiro documento que entrou na fila
        if not self.is_empty():
            documento = self._documentos.[LACUNA_2]()
            print(f"Imprimindo '{documento['nome']}' ({documento['paginas']} páginas)...")
            return documento
        print("Nenhum documento na fila de impressão.")
        return None

    def is_empty(self) -> bool:
        return len(self._documentos) == 0

# Simulação da fila de impressão
fila = FilaImpressao()
fila.adicionar_documento("relatorio.pdf", 12)
fila.adicionar_documento("artigo.docx", 5)

# Processa os documentos na ordem de chegada
fila.processar_proximo()