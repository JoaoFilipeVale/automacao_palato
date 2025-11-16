# Importar o PyTest. Este é o "motor" que vai correr
# os meus testes (as funções 'test_') e validar os meus 'asserts'.
import pytest

# Também preciso do 'By'. Este é o meu "mapa", que me deixa
# dizer *como* encontrar elementos (ex: By.ID, By.LINK_TEXT).
from selenium.webdriver.common.by import By

# Vou precisar de "Esperas Explícitas" (Explicit Waits).
# Isto é muito importante para testes de formulários, onde tenho
# de esperar que a mensagem de sucesso apareça (o que pode demorar).
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Eu importo a classe 'Select', que é a ferramenta do
# Selenium para interagir com tags <select> (dropdowns).
from selenium.webdriver.support.ui import Select


# --- Teste -> Verificar se o formulário de contacto funciona ---
def test_contact_form(driver, base_url):

    # 1. A Ação: Navegar para a página de contacto.
    driver.get(base_url + "/contacto/")


    # 2. Encontrar os elementos do formulário e preenchê-los.
    driver.find_element(By.NAME, "your-name").send_keys("Teste Automatizado")
    driver.find_element(By.NAME, "your-email").send_keys("teste@palatodigital.com")
    driver.find_element(By.NAME, "your-phone").send_keys("932001002")
    
    # 2.1. Tenho de encontro o elemento <select> do dropdown
    dropdown_element = driver.find_element(By.NAME, "your-interest")

    # 2.1.1 Passo esse elemento na ferramenta "Select"
    # para ganhar acesso aos comandos de seleção.
    select_object = Select(dropdown_element)

    # 2.1.2 Seleciono a opção que quero,
    # através do "select_by_visible_text".
    select_object.select_by_visible_text("Desenvolvimento Web")

    # Continuo a preencher o resto do formulário
    driver.find_element(By.NAME, "your-message").send_keys("Esta é uma mensagem de teste enviada por um script automatizado.")

    # 2.2. Agora tenho de encontrar a check-box das Politicas de Privacidade.
    # Necessário aceitar este passo para submetermos o formulário.
    driver.find_element(By.NAME, "acceptance-policies").click()
    

    # 3. Submeter o formulário
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


    #4. A Verificação (Assert):
    
    # Configuro uma "Espera" de 10 segundos.
    wait = WebDriverWait(driver, 10)

    # Digo ao "wait" para esperar até que o elemento
    # com a classe "wpcf7-response-output" (a caixa de resposta do CF7)
    # esteja VISÍVEL.
    error_message_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "wpcf7-response-output"))
    )

    # Finalmente, eu verifico se o texto de sucesso esperado
    # está dentro desse elemento.
    # (Verifica se esta mensagem está 100% correta!)
    expected_message = "Ocorreu um erro ao tentar enviar a sua mensagem."
    assert expected_message in error_message_element.text