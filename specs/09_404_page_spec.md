# 404 Error Page Specification

## 1. Overview
This specification defines the testing requirements for the 404 Error handling (Page Not Found).
Test implementation: `tests/test_404_page.py`

## 2. Test Scenario
Verify that navigating to a non-existent URL results in a user-friendly error page without crashing the application.

## 3. Key Verifications
1.  **Navigation**: Access a random/invalid URL (e.g., `/pagina-que-nao-existe`).
2.  **Stability**:
    - The URL should remain as requested or redirect to a specific 404 path.
    - The browser should not display a generic browser error (like "Connection Refused").
3.  **Layout**:
    - **Header**: Logo and Menu must remain visible to allow navigation.
    - **Footer**: Legal links and social icons must remain visible.
4.  **Content**:
    - A visible message indicating the error must be present.
    - **Accepted Patterns (Regex)**: "não encontrada", "nada encontrado", "erro 404", "ups".
    - Checked in H1/H2 headings OR Page Title.
