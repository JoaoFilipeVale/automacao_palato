# Cookie Policy Verification Spec

**Target URL:** `/politica-de-cookies/`

Test implementation: `tests/test_legal_pages.py`

## Test Scenarios

### 1. Verify Verification
- **Action**: Navigate to `{base_url}/politica-de-cookies/` (Note the trailing slash).
- **Assertion**:
    - URL matches expectation.

### 2. Verify Page Title
- **Action**: Locate main heading.
- **Assertion**:
    - `H2` with text "Política de Cookies do Palato Digital" (or robust substring) is visible.

### 3. Verify Key Sections
- **Action**: Locate specific headings.
- **Assertion**:
    - "1. O que são Cookies?" is visible.
    - "2. Como Utilizamos os Cookies?" is visible.
    - "Gestão de Preferências de Cookies" is visible.

### 4. Verify Cookie Management Info (Table/List)
- **Action**: Verify existence of technical cookie descriptions.
- **Assertion**:
    - Text "Cookies Necessários" is visible.
    - Text "cookieyes-consent" is visible (Evidence of technical cookie listing).
    - Text "Cookies Analíticos" is visible.
    - Text "_ga" is visible (Evidence of analytics cookie listing).

### 5. Verify Footer Visibility
- **Action**:
    - **Strictly** call `scroll_into_view_if_needed()` on `#footer-outer`.
    - Note: Based on previous findings coverage, if this fails due to 0-height, we might need `window.scrollTo`, but spec follows user request first.
- **Assertion**:
    - `#footer-outer` is visible.
