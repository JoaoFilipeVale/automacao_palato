# Palato Digital – QA Automation Framework
### UI Regression Testing with Python & Playwright

*Ensure Flawless User Experience, Effortlessly and Continuously*

![last commit](https://img.shields.io/github/last-commit/JoaoFilipeVale/automacao_palato?style=flat-square)
![languages](https://img.shields.io/github/languages/top/JoaoFilipeVale/automacao_palato?style=flat-square)

Built with the tools and technologies:

![Markdown](https://img.shields.io/badge/Markdown-1f425f?logo=markdown&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-0A9EDC?logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

---

## Overview

This repository contains the complete UI test automation framework for the **[Palato Digital](https://palatodigital.com)** website.

The goal of this project is to ensure a flawless user experience by validating critical functionalities of the website (e.g., homepage, contact form) across staging and production environments.  
Using **Python**, **Playwright**, and **PyTest**, this framework provides fast, stable, and maintainable automated regression tests.

---

## Table of Contents

- [Overview](#overview)
- [Technology Stack](#technology-stack)
- [Environment Setup](#1-environment-setup)
  - [Create Virtual Environment](#11-create-and-activate-the-virtual-environment)
  - [Generate requirements.txt](#12-generate-requirementstxt)
  - [Install Dependencies and Browsers](#13-install-dependencies-and-browsers)
- [Running Tests](#2-running-the-tests)
  - [Run All Tests](#21-run-all-tests)
  - [Run in Visible (Headed) Mode](#22-run-in-visible-mode-local-debugging)
- [Advanced Usage](#4-advanced-usage)
  - [Parallel Test Execution](#41-parallel-test-execution)
  - [Debugging and Screenshots](#42-debugging-and-screenshots)
  - [CI/CD Integration](#43-cicd-integration)
- [Project Structure](#3-project-structure)
- [Final Notes](#final-notes)

---

## Technology Stack

- **Language:** Python 3.12+
- **Test Framework:** PyTest
- **Automation Library:** Playwright (modern, fast, and reliable)
- **Browser Engines:** Chromium (default), WebKit, Firefox
- **CI Support:** GitHub Actions (optional)

---

## 1. Environment Setup

Before running tests, prepare your environment.

### 1.1. Create and Activate the Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source venv/bin/activate
```

### 1.2. Freeze Dependencies (requirements.txt)
To register the project dependencies, freeze them into a file.

```bash
pip freeze > requirements.txt
```

### 1.3. Install Dependencies and Browsers

```bash
# Install dependencies
pip install -r requirements.txt

# Install browser binaries (Chromium is default)
playwright install chromium
```

---

## 2. Running the Tests

The framework supports multi-environment execution via the `--env` flag.

### 2.1. Run All Tests (Staging by Default)

```bash
pytest
```

To run against Production:

```bash
pytest --env=prod
```

You can also run individual tests:

```bash
pytest tests/test_homepage_title.py
```

### 2.2. Run in Visible Mode (Local Debugging)

```bash
pytest --headed
```

---

## 4. Advanced Usage

### 4.1. Parallel Test Execution

Run tests in parallel to speed up execution using **pytest-xdist**:

```bash
pip install pytest-xdist
pytest -n auto
```

- `-n auto` automatically uses all available CPU cores.

### 4.2. Debugging and Screenshots

- To pause tests and debug interactively:

```bash
pytest --headed --pause
```

- To automatically capture screenshots on failure:

```python
# Example in conftest.py fixture
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.failed:
        page.screenshot(path=f"screenshots/{item.name}.png")
```

### CI/CD Integration (GitHub Actions Example)

Create `.github/workflows/test.yml`:

```yaml
name: Playwright Tests

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4 # Use v4 is safer
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install Dependencies
        run: |
          # The Runner shell is already active. No need for venv commands here.
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          playwright install
      - name: Run Tests
        # Playwright runs HEADLESS by default on CI
        run: |
          pytest --env=stag
```

---

## 3. Project Structure

```
automacao_palato/
│
├── venv/                  # Virtual environment
│
├── tests/                 # All test files
│   ├── __init__.py
│   ├── test_homepage_title.py
│   └── test_contact_form.py
│
├── conftest.py            # Global fixtures, env selection logic
│
└── requirements.txt       # Dependencies list
```

---

## Final Notes

This framework ensures Palato Digital’s platform remains stable, reliable, and user‑friendly across updates.

Feel free to open issues or contribute with improvements!

