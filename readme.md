# Framework de Automação de Testes (Palato Digital)

Este repositório contém o *framework* de automação de testes de QA para o website **Palato Digital**.

O objetivo principal deste projeto é criar um conjunto de testes de regressão (UI) para validar a funcionalidade principal do site (como o formulário de contacto) após atualizações, garantindo que novas versões de *plugins* ou temas não "partem" o site em produção.

---

## Stack de Tecnologias (O que este projeto usa)

- **Linguagem:** Python 3.12+
- **Framework de Testes:** PyTest (para gestão, execução, *fixtures* e *asserts*)
- **Automação de Browser:** Selenium WebDriver
- **Gestão de Drivers:** `webdriver-manager` (para gerir o `chromedriver` automaticamente)

---

## 1. Preparação do Ambiente

Antes de correr os testes pela primeira vez, precisas de preparar o teu ambiente local.

### 1.1. Criar e Ativar o Ambiente Virtual

É uma boa prática isolar as dependências do projeto.

```bash
# 1. Cria o ambiente virtual (venv)
python -m venv venv

# 2. Ativa o ambiente:
# Windows (PowerShell):
.env\Scripts\Activate.ps1

# Mac/Linux (Bash/Zsh):
source venv/bin/activate
```

### 1.2. Criar o requirements.txt (Apenas uma vez)

Para sabermos quais são as dependências do projeto, vamos "congelá-las" num ficheiro.

```bash
pip freeze > requirements.txt
```

### 1.3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

---

## 2. Executar os Testes

A framework permite correr testes em diferentes ambientes usando `--env`.

### 2.1. Correr todos os testes

Staging (default):

```bash
pytest
```

Produção:

```bash
pytest --env=prod
```

### 2.2. Correr um ficheiro de teste específico

```bash
pytest tests/test_contact_form.py --env=stag
pytest tests/test_homepage_title.py --env=prod
```

---

## 3. Estrutura do Projeto

```
automacao_palato/
|
├── .venv/                  
|
├── tests/                  
|   ├── __init__.py         
|   ├── test_homepage_title.py
|   └── test_contact_form.py
|
├── conftest.py             
|
└── requirements.txt        
```
