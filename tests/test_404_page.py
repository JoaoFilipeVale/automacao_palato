from playwright.sync_api import Page, expect
import re

def test_404_page(page: Page, base_url, layout):
    """
    Test Scenario: Verify behavior when navigating to a non-existent URL.
    
    Steps:
    1. Navigate to a random/invalid URL (e.g., /pagina-que-nao-existe).
    2. Verify that the URL remains as requested (or redirects to a 404 page).
    3. Verify that the standard Header and Footer are still visible (User Experience).
    4. Verify the presence of a "Not Found" message or 404 indication.
    """

    # 1. Navigate to Invalid URL
    invalid_url = f"{base_url}/pagina-que-nao-existe-12345"
    page.goto(invalid_url)
    
    # Wait for load - 404 pages might be lighter/faster or standard WP pages
    page.wait_for_load_state("domcontentloaded")

    # 2. Verify URL
    # We expect the URL to be what we requested (WordPress usually keeps the URL) 
    # OR redirect to a specific 404 page.
    # The important part is that we didn't crash.
    expect(page).to_have_url(re.compile(r".*/pagina-que-nao-existe-12345"))

    # 3. Verify Layout (Header & Footer)
    # Even on error pages, the user should be able to navigate.
    layout.verify_header()
    layout.verify_footer()

    # 4. Verify 404 Indication
    # We check for common Portuguese 404 text.
    # "Página não encontrada", "Erro 404", "Nada encontrado", "Ups!"
    # We use a broad regex to catch likely candidates visible on the page.
    error_message_regex = re.compile(r"não encontrada|nada encontrado|erro 404|ups", re.IGNORECASE)
    
    # We check the Main Heading or the Page Title
    heading = page.get_by_role("heading", name=error_message_regex).first
    title = page.title()
    
    # Assert that either the title or a visible heading confirms the 404 status
    if not heading.is_visible():
        assert error_message_regex.search(title), f"Title '{title}' does not contain expected 404 text."
    else:
        expect(heading).to_be_visible()
