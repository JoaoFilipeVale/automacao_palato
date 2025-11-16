# Importo o PyTest. Eu preciso disto para
# que o PyTest reconheça as minhas funções especiais,
# como "pytest_addoption" e o '@pytest.fixture'.
import pytest

# Importar as ferramentas do Selenium (webdriver, Service)
# e o gestor (ChromeDriverManager) aqui,
# porque a minha fixture 'driver' (que abre o browser) vai usar isto
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# --- Adicionar a minha opção '--env' ao PyTest ---

# Esta é uma função "hook" do PyTest. O PyTest vai
# procurá-la e executá-la automaticamente quando eu arrancar os testes.
# O "parser" é o objeto que me vai permitir "adicionar novas opções"
# à minha linha de comandos.
def pytest_addoption(parser):
    """Esta função vai registar a minha opção '--env' personalizada no PyTest"""

    # Aqui vou adicionar a minha própria flag da linha de comandos.
    parser.addoption(
        # O nome da minha flag (exemplo --env=prod)
        "--env",

        # A ação: "store" significa "guarda o valor que vem a seguir"
        # (exemplo --env="prod" -> eu quero que ele armazene "prod").
        action="store",

        # O valor padrão: Se eu correr só "pytest" sem
        # a flag '--env', quero que o valor "stag" seja usado por defeito.
        default="stag",

        # Mensagem de ajuda que vai aparecer se eu correr "pytest --help"
        help="O ambiente que os meus testes devem correr (exemplo 'stag' ou 'prod')"
    )


# --- Criar a minha fixture "base_url" ---

# O "@pytest.fixture" é um "decorador". Vou usá-lo para transformar
# esta função num "assistente" que pode "fornecer" o URL
# a qualquer teste que o peça.
@pytest.fixture
def base_url(request: pytest.FixtureRequest):
    """Esta fixture vai ler a minha opção '--env' do terminal e devolver o URL correto"""

    # "request" é um argumento especial do PyTest
    # vai dar-me acesso ao "contexto" do teste, incluindo as
    # opções da linha de comandos que eu acabei de definir.
    
    # 1. Vou ler o valor que eu passei (exemplo "stag" ou "prod")
    env = request.config.getoption("--env")

    # 2. Vou definir os meus URLs num dicionário (é mais limpo)
    urls = {
        "stag": "https://stag.palatodigital.com", # URL Desenvolvimento
        "prod": "https://palatodigital.com" # URL Produção
    }

    # 3. Tratamento de Erro:
    # Vou verificar se o "env" que eu escrevi existe nos meus URLs.
    # Isto é importante para falhar "rapidamente" se eu me enganar
    # (exemplo --env=producao)
    if env not in urls:
        raise pytest.UsageError(f"Ambiente '{env}' desconhecido. Válidos: {list(urls.keys())}")
    
    # 4. Devolver o URL correcto.
    # Qualquer teste que eu escrever que peça "base_url" como argumento
    # (exemplo def test_foo(base_url): ...)
    # vai receber o URL que esta linha retornar.
    return urls[env]



# --- Criar a minha fixture "driver" ---

# O '@pytest.fixture' transforma esta função num "assistente" global para todos os testes.
@pytest.fixture
def driver():
    """Esta fixture vai abrir e fechar o browser para os meus testes"""

    # 1. Configuro o ChromeDriver automaticamente.
    # Vou usar o ChromeDriverManager().install() para ele descarregar
    # o driver correto para a minha versão do Chrome.
    s = Service(ChromeDriverManager().install())

    # 2. Agora, vou iniciar o browser Chrome,
    # dizendo-lhe para usar o "Service" que acabei de configurar.
    driver = webdriver.Chrome(service=s)

    # 3. O meu site (Wordpress) pode demorar a carregar elementos.
    # Para tornar os meus testes mais estáveis, vou adicionar uma
    # espera implícita de 5 segundos.
    driver.implicitly_wait(5)

    # 4. Esta é a parte central da fixture: o 'yield'.
    # Eu "entrego" o "driver" (o browser) ao teste que o pediu.
    yield driver

    # 5. Depois que o teste acabar, eu volto aqui.
    # Esta parte do código vai fechar o browser,
    # garantindo que não fiquem janelas abertas depois dos testes.
    driver.quit()