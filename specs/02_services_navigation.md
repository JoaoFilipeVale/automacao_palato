# Test Scenario: Services Page Navigation

## Goal
Verify that the `Serviços` page is accessible from the homepage and displays the correct content, including specific headings and the first service offering.

## Target URL
`https://palatodigital.com/` (Start) -> `https://palatodigital.com/servicos/` (Destination)

## Elements Identification

### Homepage
- **Navigation Menu Link**:
  - Text: "Serviços"
  - Location: Main Header

### Services Page (`/servicos/`)
- **Main Heading (H1)**:
  - Exact Text: "Serviços"
  - Visibility: Must be visible.
- **Sub-heading / Label**:
  - Text: "O que fazemos"
  - Location: Immediately above the H1.
- **First Service Card**:
  - Title: "Estratégia e inovação digital" (Note: may contain icon like "💡").
  - Verification Strategy: Check for text containment if icon is present.
- **Header & Footer**:
  - Must remain visible after navigation.

## Steps to Execute

1.  **Navigate to Homepage**
    - **Action**: Open base URL.
    - **Validation**: Page loads.

2.  **Click 'Serviços'**
    - **Action**: Locate the "Serviços" link in the header and click it.
    - **Validation**: URL changes to include `/servicos/`.

3.  **Verify Headings**
    - **Action**: Locate H1 and the sub-heading above it.
    - **Validation**:
        - H1 has text "Serviços".
        - Element above H1 has text "O que fazemos".

4.  **Verify Service Cards**
    - **Action**: Locate the service cards in the grid.
    - **Validation**: Ensure ALL of the following core services are visible:
        - "Estratégia e inovação digital"
        - "Identidade e design da marca"
        - "Desenvolvimento Web"
        - "Alojamento e domínios"
        - "Suporte e manutenção contínuos"

5.  **Verify Layout Consistency**
    - **Action**: Check for Header and Footer presence.
    - **Validation**: Both are visible.
