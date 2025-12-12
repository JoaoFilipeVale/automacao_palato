# Privacy Policy Navigation Test Specification

Test implementation: `tests/test_legal_pages.py`

**Target URL:** `/politica-de-privacidade`

## Test Scenarios

### 1. Verify Successful Navigation
- **Action**: Navigate to `{base_url}/politica-de-privacidade`.
- **Assertion**:
    - HTTP response status is 200 (implicitly verified by Playwright not throwing an error on navigation, but explicit URL check confirms we are on the page).
    - URL ends with `/politica-de-privacidade`.

### 2. Verify Page Title
- **Action**: Locate the main heading.
- **Assertion**:
    - The `h1` (or `h2` if styled as main title) contains text "Política de Privacidade".
    - *Note from analysis*: The page uses an H2 with text "Política de Privacidade do Palato Digital" as the main visual title in the content body.

### 3. Verify Critical Text Blocks
- **Action**: Locate key legal sections.
- **Assertion**:
    - "1. Informações que Recolhemos" is visible.
    - "2. Finalidade da Utilização dos Dados" is visible.
    - "5. Direito dos Utilizadores" is visible.
    - "8. Contacto sobre a Política de Privacidade" is visible.

### 4. Verify Footer Visibility
- **Action**: Scroll to bottom.
- **Assertion**:
    - The global footer is visible (standard check for all pages).
