# Strings
# Cenário. Um formulário de cadastro recebeu a frase de apresentação de um usuário cheia de pontuação e espaçamento inconsistente. Antes de armazenar, o time de dados quer normalizar o texto para um formato padrão.
# Tarefa: Leia uma frase, remova a pontuação básica e mostre as palavras em maiúsculas, separadas por vírgula.

import string

# Frase recebida do formulário
frase = "Olá, mundo! Este é um teste... de formatação."

#remover pontuacao
tabela = str.maketrans("", "", string.punctuation)
texto_limpo = frase.translate(tabela)

print(texto_limpo)

#maiuscula
# texto_maiusculo = texto_limpo.upper()
# print(texto_maiusculo)

# #virgula
# separado_virgula = texto_maiusculo.split()
# print(separado_virgula)

#list comprehention
palavras = [p.upper() for p in texto_limpo.split()]
print(palavras)

#unir
resultado = ", ".join(palavras)
print(resultado)