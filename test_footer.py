from playwright.sync_api import sync_playwright

def test_footer_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://only.digital/", timeout=60000)

        # Ждём появления футера
        footer = page.locator("footer")
        footer.wait_for(state="visible", timeout=10000)

        # Проверяем логотип
        footer_logo = footer.locator("img")
        assert footer_logo.count() > 0, "Логотип в футере не найден"

        browser.close()
