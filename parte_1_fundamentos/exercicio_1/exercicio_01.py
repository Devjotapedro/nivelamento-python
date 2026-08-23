#Entredas e tipos

# Cenário. Uma escola quer digitalizar as fichas de matrícula. Antes de montar qualquer sistema, é preciso garantir que os dados básicos de um aluno — nome, idade e nota final — possam ser lidos do teclado e exibidos de volta corretamente, cada um no tipo certo.
# Tarefa: Escreva um programa que leia nome, idade e nota final de um aluno (com input()), convertendo cada valor para o tipo apropriado (int para idade, float para nota). Imprima uma mensagem formatada reunindo os três dados.

def ler_exibir_dados_alunos():
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    nota = float(input('Digite a nota do aluno: '))
    
    return f'Nome: {nome} | idade: {idade} | Nota: {nota:.1f}'
    
dados = ler_exibir_dados_alunos() 
print(dados)  