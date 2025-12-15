from playwright.sync_api import sync_playwright

def test_footer_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://only.digital/", timeout=60000)

        # Ждём футер
        footer = page.locator("footer")
        footer.wait_for(state="visible", timeout=20000)

        # Проверяем, что футер содержит хотя бы одну ссылку
        links = footer.locator("a")
        assert links.count() > 0, "Ссылки в футере не найдены"

        # Проверяем, что футер содержит текст (например ©)
        footer_text = footer.inner_text()
        assert "©" in footer_text, "Текст футера не найден"

        browser.close()
