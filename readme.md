# Test Automation Framework (Palato Digital)

This repository contains the QA test automation framework for the **[Palato Digital](https://palatodigital.com)** website.

The main goal of this project is to create a UI regression test suite that validates the website’s core functionality (such as the contact form) after updates, ensuring that new plugin or theme versions do not break the production site.

---

## Technology Stack (What this project uses)

- **Language:** Python 3.12+
- **Test Framework:** PyTest (for test management, execution, fixtures, and assertions)
- **Browser Automation:** Selenium WebDriver
- **Driver Management:** `webdriver-manager` (to automatically manage the ChromeDriver)

---

## 1. Environment Setup

Before running the tests for the first time, you need to prepare your local environment.

### 1.1. Create and Activate the Virtual Environment

It's a good practice to isolate project dependencies.

```bash
# 1. Create the virtual environment (venv)
python -m venv venv

# 2. Activate the environment:
# Windows (PowerShell):
venv\Scripts\Activate.ps1

# macOS/Linux (Bash/Zsh):
source venv/bin/activate
```

### 1.2. Generate requirements.txt (Only once)

To register the project dependencies, freeze them into a file.

```bash
pip freeze > requirements.txt
```

### 1.3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Running the Tests

The framework supports running tests against different environments by using the `--env` flag.

### 2.1. Run all tests

Staging environment (default):

```bash
pytest
```

Production:

```bash
pytest --env=prod
```

### 2.2. Run a specific test file

```bash
pytest tests/test_contact_form.py --env=stag
pytest tests/test_homepage_title.py --env=prod
```

---

## 3. Project Structure

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
