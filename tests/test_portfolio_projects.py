import pytest
import re
from playwright.sync_api import Page, expect

# Data for Portfolio Projects
# Format: (project_slug, project_title, expected_subsections, website_url)
PORTFOLIO_PROJECTS = [
    (
        "patinhasyes", 
        "PatinhasYes", 
        ["O que fizemos", "Tipo de negócio", "Website", "Descrição"],
        "https://patinhasyes.pt"
    ),
    (
        "alcmena", 
        "Alcmena", 
        ["O que fizemos", "Tipo de negócio", "Website", "Descrição"],
        "https://alcmena.pt"
    )
]

@pytest.mark.parametrize("project_slug, project_title, expected_subsections, website_url", PORTFOLIO_PROJECTS)
def test_portfolio_project_content(page: Page, base_url, layout, project_slug, project_title, expected_subsections, website_url):
    """
    Parametrized test to verify the content and layout of Portfolio Project pages.
    """
    # 1. Navigation
    target_url = f"{base_url}/portfolio/{project_slug}/"
    page.goto(target_url)
    page.wait_for_load_state("domcontentloaded")
    
    # Check URL
    expect(page).to_have_url(re.compile(f".*/portfolio/{project_slug}/?$"))

    # 2. Verify Page Title (H1)
    # The project name should be the main heading
    expect(page.get_by_role("heading", name=project_title, exact=True).first).to_be_visible()

    # 3. Verify Key Subsections (H5)
    for section in expected_subsections:
        expect(page.get_by_role("heading", name=section, exact=False).first).to_be_visible()

    # 4. Verify External Website Link
    if website_url:
        # We look for a link that matches the website URL
        # Often labeled as the project name or "Website"
        project_link = page.get_by_role("link", name=re.compile(r"Alcmena\.pt|PatinhasYes", re.IGNORECASE))
        # Ensure at least one link pointing to the external site exists and is visible
        external_link = page.locator(f"a[href='{website_url}']").first
        expect(external_link).to_be_visible()

    # 5. Verify Layout (Header & Footer)
    layout.verify_header()
    layout.verify_footer()

    # 6. Verify "Explore mais" Section existence
    expect(page.get_by_text("Explore mais", exact=False).first).to_be_visible()
