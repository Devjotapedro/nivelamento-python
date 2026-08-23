#Type hints e formatação

# Cenário. Um sensor de temperatura importado dos EUA só relata valores em Celsius, mas o relatório final do laboratório precisa estar em Fahrenheit, a unidade usada pelo cliente.
# Tarefa: Implemente celsius_para_fahrenheit(c: float) -> float. Leia uma temperatura em Celsius e exiba o resultado convertido, formatado com duas casas decimais.

def celsius_para_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

graus = float(input('Digite o valor em celsius: '))
fh = celsius_para_fahrenheit(graus)
print(f'{graus} celsius em fahrenheit é {fh}')