# Classes e dataclasses
# Cenário. Uma loja quer controlar o valor total do seu estoque: para cada produto, é preciso saber o preço, quantas unidades existem e quanto isso representa em reais.
# Tarefa: Modele um Produto com @dataclass (nome, preco, estoque) e implemente o método valor_total(), que retorna preco * estoque.

from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int
    
    def valor_total(self) -> float:
        return self.preco * self.estoque
    

# Exemplo de uso
item = Produto(nome="Teclado Mechanical", preco=250.0, estoque=10)
print(f"Produto: {item.nome}")
print(f"Valor total em estoque: R$ {item.valor_total():.2f}")