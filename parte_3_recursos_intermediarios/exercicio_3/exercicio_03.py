# Módulos e testes
# Cenário. Uma aplicação carrega configurações de um arquivo JSON escrito por outra pessoa da equipe. Antes de confiar nesses dados, é preciso validar que o arquivo existe e está no formato esperado — e garantir, com testes, que essa validação continua funcionando conforme o projeto evolui.
# Tarefa: Crie um módulo que valide e carregue um JSON de dados. Escreva ao menos um teste pytest cobrindo uma entrada válida e uma entrada inválida.

import json

def carregar_configuracoes(caminho_arquivo: str) -> dict:
    # Abertura e leitura do arquivo JSON
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    
    # Validação simples: verifica se possui a chave obrigatória 'ambiente'
    if "ambiente" not in dados:
        raise ValueError("Chave 'ambiente' ausente na configuração")
        
    return dados