# Test Plan: Homepage Sanity Check

## Goal
Verify that the `palatodigital.com` homepage works as expected by checking the visibility and functionality of all main buttons and links.

## Target URL
`https://palatodigital.com/`

## Analyzed Sections & Elements

### 1. Header Navigation
The main menu is located at the top of the page.
- **Logo**: Should be visible and link to the homepage.
- **Menu Links**:
    - "Portfólio" -> Should link to the portfolio section/page.
    - "Serviços" -> Should link to the services section/page.
    - "Sobre" -> Should link to the about section/page.
    - "Vamos falar" (CTA in Header) -> Should link to `/contacto/`.
- **Language Switcher**: Should be present (usually displaying "PT" or "EN").

### 2. Main Content (Hero & Body)
- **Primary Call-to-Action (CTA)**:
    - Text: "Vamos falar" (often located under "Tem um projeto em mente?" or similar heading).
    - Expected Behavior: Links to `/contacto/`.
- **Cookie Consent**:
    - Check if the cookie banner appears and if the "Aceitar" / "Aceite tudo" button functions.

### 3. Footer
Located at the bottom of the page.
- **Social Media Links**:
    - Instagram
    - Facebook
    - LinkedIn
    - Behance
    - *Verification*: Check if these links are visible and have valid `href` attributes pointing to the respective social platforms.
- **Legal Links**:
    - "Politica de Privacidade"
    - "Politica de Cookies"
    - "Termos e Condições"
    - *Verification*: Ensure these links are visible.

## Test Scenario: Comprehensive Homepage Sanity

### Steps to Execute

1.  **Load Homepage**
    - Go to `https://palatodigital.com/`.
    - Verify page title contains "Palato".

2.  **Cookie Banner Handling**
    - Identify if the cookie banner is present.
    - Verify the "Aceitar" button is clickable.
    - Click it and ensure the banner disappears.

3.  **Header Verification**
    - **Logo**: Verify visibility.
    - **Navigation Links**: Iterate through "Portfólio", "Serviços", "Sobre", "Vamos falar".
        - Verify they are visible.
        - Verify they are clickable (or have valid `href`).

4.  **Body CTA Verification**
    - Scroll to the main body CTA ("Tem um projeto em mente?").
    - Verify the "Vamos falar" button/link is visible and points to `/contacto/`.

5.  **Footer Verification**
    - Scroll to the footer.
    - **Social Media**: Verify that Instagram, Facebook, LinkedIn, and Behance icons/links are present.
    - **Legal**: Verify "Politica de Privacidade", "Politica de Cookies", "Termos e Condições" are present.

### Success Criteria
- All identified elements are found on the page.
- No visibility errors (elements overlapping or hidden unexpectedly).
- Critical links (especially "Vamos falar") have the correct destination.
