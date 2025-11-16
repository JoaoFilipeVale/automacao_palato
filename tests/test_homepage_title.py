# Importar o PyTest. Este é o "motor" que vai correr
# os meus testes (as funções 'test_') e validar os meus 'asserts'.
import pytest


# --- Teste -> Verificar o título da página principal do site ---

# O meu teste pede "driver" e "base_url".
# O PyTest vai buscar AMBAS as fixtures ao ficheiro "conftest.py"
def test_homepage_title(driver, base_url):
    
    # 1. A Ação: Abrir o URL que o 'base_url' me deu
    driver.get(base_url)

    # 2. A Verificação (Assert):
    
    # Eu defino o título exato que eu espero que a página tenha.
    expected_title = "Palato Digital – O sabor da inovação digital"

    # Eu "afirmo" que o título real (driver.title) é igual ao esperado.
    assert driver.title == expected_title