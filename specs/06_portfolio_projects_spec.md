# Portfolio Project Specification

## 1. Overview
This specification defines the testing requirements for individual Portfolio Project pages. The structure is consistent across all projects.

- **URL Pattern**: `/portfolio/{project-slug}/`
- **Example**: `/portfolio/patinhasyes/`, `/portfolio/alcmena/`

Test implementation: `tests/test_portfolio_projects.py`

## 2. Key Sections to Verify
1.  **Project Title**: The h1 heading with the project name (e.g., "PatinhasYes").
2.  **"O que fizemos" Section**: Subsection detailing services.
3.  **Project Details**:
    - **"Tipo de negócio"**: Classification.
    - **"Website" Link**: External link to the live project (if applicable).
    - **"Descrição"**: Detailed case study text.
4.  **"Explore mais" Section**: Navigation to other projects.
5.  **CTA Section**: "Tem um projeto em mente? Vamos falar".

## 3. Layout Verification
- **Header**: Logo and Menu visible.
- **Footer**: Footer visible.
