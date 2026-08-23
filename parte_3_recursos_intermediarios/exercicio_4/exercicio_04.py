# CLI
# Cenário. Antes de processar um arquivo de log gigante, um analista quer uma forma rápida de conferir, pelo terminal, quantas linhas ele tem — sem abrir o arquivo em um editor de texto.
# Tarefa: Implemente um script CLI que receba --arquivo e imprima o número de linhas do arquivo, tratando o erro de arquivo ausente com uma mensagem clara.

import argparse

def contar_linhas():
    # Configuração do analisador de argumentos da CLI
    parser = argparse.ArgumentParser(description="Conta o número de linhas de um arquivo.")
    parser.add_argument("--arquivo", required=True, help="Caminho para o arquivo de log")
    
    args = parser.parse_args()

    # Leitura e contagem de linhas com tratamento de exceções
    try:
        with open(args.arquivo, "r", encoding="utf-8") as file:
            linhas = sum(1 for _ in file)
            print(f"O arquivo '{args.arquivo}' possui {linhas} linhas.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{args.arquivo}' não foi encontrado.")

if __name__ == "__main__":
    contar_linhas()