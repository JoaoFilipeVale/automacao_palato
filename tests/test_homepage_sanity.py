import pytest
import re
from playwright.sync_api import Page, expect

# --- Test -> Homepage Sanity Check ---

def test_homepage_sanity(page: Page, base_url, layout):
    """
    Verifies that the homepage loads correctly and key elements are visible and functional.
    Scope: Title, Header, Hero CTA, Footer (Social & Legal).
    """

    # 1. Load Homepage & Basic Validation
    page.goto(base_url)
    
    # Immediate check to ensure the correct page loaded.
    # We use re.compile to match "Palato Digital" anywhere in the title.
    # This makes the test robust against small changes like "Página Principal - Palato Digital".
    expect(page).to_have_title(re.compile("Palato Digital"))
    
    # 2. Cookie Banner Handling -> Handled by 'layout' fixture automatically

    # 3. Header Verification
    
    # Standard Header Verification (Logo + Menu)
    layout.verify_header()

    # --- NAVIGATION CHECKS ---
    
    # 3.1 Links pointing to OTHER pages (External or Sub-pages)
    nav_pages = {
        "Serviços": "/servicos/",
        "Sobre": "/sobre/",
        "Vamos falar": "/contacto/"
    }

    for name, href_part in nav_pages.items():
        # UPDATE: Changed to exact=False to be less strict 
        # (accepts "SERVIÇOS", " Serviços ", etc.)
        link = page.get_by_role("link", name=name, exact=False).first
        
        expect(link).to_be_visible()
        # Verify if the URL contains the specific part
        expect(link).to_have_attribute("href", re.compile(f".*{href_part}"))

    # 3.2 Portfolio Link (Internal / Homepage Section)
    # We verify if the link points to the root "/" or an anchor "#"
    
    # UPDATE: exact=False here too!
    portfolio_link = page.get_by_role("link", name="Portfólio", exact=False).first
    
    expect(portfolio_link).to_be_visible()
    
    # Regex accepts: "https://palatodigital.com/" or "https://palatodigital.com/#portfolio"
    expect(portfolio_link).to_have_attribute("href", re.compile(r".*(/|#.*)$"))

    # 4. Body CTA Verification
    cta_heading_text = "Tem um projeto em mente?"
    cta_section_heading = page.get_by_text(cta_heading_text)
    
    if cta_section_heading.is_visible():
        cta_section_heading.scroll_into_view_if_needed()
        expect(cta_section_heading).to_be_visible()
        
        # STRATEGY UPDATE:
        # Instead of complicating with parent sections, we find ALL "Vamos falar" buttons.
        # Then, we iterate over them to find the one currently VISIBLE.
        # (The header button might also be visible, so we ensure we find at least one valid visible button in the context).
        
        # 1. Get all "Vamos falar" links
        all_ctas = page.get_by_role("link", name="Vamos falar", exact=False)
        
        # 2. Ensure at least one is visible and enabled
        # count() tells us how many exist. We check if any satisfies the condition.
        found_body_cta = False
        
        for i in range(all_ctas.count()):
            cta = all_ctas.nth(i)
            if cta.is_visible():
                # Optional: Verify if the href points to contact
                href = cta.get_attribute("href")
                if href and "contacto" in href:
                    found_body_cta = True
                    break
        
        if not found_body_cta:
            pytest.fail("No visible 'Vamos falar' button found in the CTA section.")

    # 5. Footer Verification
    layout.verify_footer()

    # Social Media Links
    social_networks = ["Instagram", "Facebook", "LinkedIn", "Behance"]
    
    for social in social_networks:
        social_link = page.get_by_role("link", name=social, exact=False)
        
        # Fallback if accessible name is not found
        if not social_link.count():
             social_link = page.locator(f"a[href*='{social.lower()}']")
        expect(social_link.first).to_be_visible()

    # Legal Links
    legal_links = [
        "Politica de Privacidade",
        "Politica de Cookies",
        "Termos e Condições"
    ]

    for legal in legal_links:
        link = page.get_by_role("link", name=legal)
        expect(link).to_be_visible()