# Dicionários
# Cenário. Um professor de linguística quer saber, rapidamente, quais vogais aparecem com mais frequência em um texto, para comparar a sonoridade de diferentes trechos.
# Tarefa: Escreva uma função que conte a frequência de cada vogal em uma string e retorne um dict com o resultado (vogal → quantidade de ocorrências).

def contar_vogais(texto: str) -> dict:
    texto = texto.lower()
    
    #inicializar um dicionário
    contagem = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for c in texto:
        if c in contagem.keys():
            contagem[c] += 1
    return contagem

frase = 'Lula e ladrao'
contador = contar_vogais(frase)
print(contador)