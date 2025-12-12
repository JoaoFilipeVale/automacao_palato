# Test Scenario: Full Contact Page Verification

## Goal
Verify the "Contacto" page content, including static contact details, and execute the contact form submission logic.

## Target URL
`https://palatodigital.com/` (Start) -> `https://palatodigital.com/contacto/` (Destination)

## Elements Identification

### Homepage
- **Header CTA**: "Vamos falar" link.
  - Action: Click to navigate.

### Contact Page (`/contacto/`)
- **Main Heading (H1)**:
  - Exact Text: "Contacto"
- **Introductory Text**:
  - Sample: "Quer tenha uma ideia clara ou apenas queira explorar possibilidades..."
  - Verification: Check for visibility of partial text.
- **Contact Details**:
  - Email: `geral@palatodigital.com` (Must be visible).
  - Phone: *Not found on page* (Do not verify).
- **Contact Form**:
  - Valid Fields: Name, Email, Phone (optional), Subject (optional), Message.

## Steps to Execute

1.  **Navigate to Homepage**
    - Action: Open base URL.

2.  **Navigation**
    - Action: Click the "Vamos falar" button/link in the Header.
    - Validation: URL changes to include `/contacto/`.

3.  **Static Content Verification**
    - **H1**: Verify text "Contacto" is visible.
    - **Intro Text**: Verify intro text containing "quer tenha uma ideia clara" is visible.
    - **Email**: Verify `geral@palatodigital.com` is visible.

4.  **Form Execution**
    - **Action**: Execute the existing form filling and validation logic.
    - *Note*: This step implies filling the form and checking the success/error message as per previous contact form tests.
