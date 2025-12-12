# Test Scenario: About Page Navigation and Content

## Goal
Verify that the `Sobre` (About) page is accessible from the homepage and displays the correct core content and philosophy.

## Target URL
`https://palatodigital.com/` (Start) -> `https://palatodigital.com/sobre/` (Destination)

## Elements Identification

### Homepage
- **Navigation Menu Link**:
  - Text: "Sobre"
  - Location: Main Header

### About Page (`/sobre/`)
- **Main Heading (H1)**:
  - Text: 'O "Palato" por trás do Digital'
  - Verification: Check for visibility and text content.
- **Intro Text**:
  - Content: "O Palato Digital é o seu parceiro especialista na construção de ecossistemas digitais..."
  - Verification Strategy: Use `get_by_text` with partial string.
- **Sections**:
  - "A nossa filosofia" (Heading or visible text).
- **Philosophy Cards**:
  - Card 1: 'Parceiros, não fornecedores'
  - Card 2: 'Performance, não “moda”'
  - Card 3: 'Design, não decoração'
  - Verification Strategy: Use `get_by_text` or `get_by_role` if they are headings. Ensure text presence.
- **Header & Footer**:
  - Must remain visible.

## Steps to Execute

1.  **Navigate to Homepage**
    - **Action**: Open base URL.
    - **Validation**: Page loads.

2.  **Click 'Sobre'**
    - **Action**: Click the "Sobre" link in the header.
    - **Validation**: URL changes to include `/sobre/`.

3.  **Verify Main Content**
    - **Action**: Check H1 and Intro Text.
    - **Validation**:
        - H1 is visible and matches 'O "Palato" por trás do Digital'.
        - Intro text is visible.

4.  **Verify Philosophy Section**
    - **Action**: Scroll to 'A nossa filosofia'.
    - **Validation**:
        - Section title visible.
        - All 3 cards visible with correct titles.

5.  **Verify Layout Consistency**
    - **Action**: Check for Header and Footer presence.
    - **Validation**: Both are visible.
