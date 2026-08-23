#Função e condicional
# Cenário. Um professor calcula a média de três notas e decide a situação de cada aluno manualmente, um por um. Com uma turma de 40 alunos, isso é lento e sujeito a erro — ele quer uma função que faça esse cálculo de forma confiável e reutilizável.

# Tarefa: Implemente calcular_media(n1: float, n2: float, n3: float) -> float e use-a para decidir a situação do aluno: Aprovado (média ≥ 7), Recuperação (média ≥ 4) ou Reprovado (caso contrário).

def calcular_media(n1: float, n2: float, n3: float) -> float:
    media = (n1 + n2 + n3)/3
    return media
    
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
    
media = calcular_media(n1, n2, n3)

if media >= 7:
    situacao = 'APROVADO'
elif media >= 4:
    situacao = 'RECUPERACAO'
else:
    situacao = 'REPROVADO'

print(f'Média: {media:.1f} - Situação: {situacao}')