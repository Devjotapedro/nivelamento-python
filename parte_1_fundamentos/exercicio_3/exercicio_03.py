#Repetição

# Cenário. Durante uma prova, o professor vai anotando as notas da turma conforme os alunos entregam — sem saber de antemão quantos vão entregar. Combinou-se que digitar 0 sinaliza o fim da coleta.
# Tarefa: Crie um laço que leia números até o usuário digitar 0. Ao final, imprima a soma, a média, o maior e o menor número lidos (ignorando o 0 do sinalizador de parada).

notas = []

while True:
    nota = float(input('Digite a nota do aluno (ou 0 para parar): '))
    
    if nota == 0:
        break
    notas.append(nota)
    
    soma = sum(notas)
    media = soma/len(notas)
    maior = max(notas)
    menor = min(notas)
    
print(f'Soma: {soma} | media: {media} | maior: {maior} | menor: {menor}')