import pytest
# Importa a função do arquivo de exercício
from exercicio_03 import carregar_configuracoes 

def test_carregar_configuracao_valida(tmp_path):
    arquivo_valido = tmp_path / "config.json"
    arquivo_valido.write_text('{"ambiente": "producao", "porta": 8080}', encoding="utf-8")
    
    # Corrigido o nome da função (plural)
    resultado = carregar_configuracoes(str(arquivo_valido)) 
    assert resultado["ambiente"] == "producao"

def test_carregar_configuracao_invalida(tmp_path):
    arquivo_invalido = tmp_path / "config_ruim.json"
    arquivo_invalido.write_text('{"porta": 8080}', encoding="utf-8")
    
    # Corrigido de 'catch' para 'raises' e corrigido o nome da função
    with pytest.raises(ValueError): 
        carregar_configuracoes(str(arquivo_invalido))
