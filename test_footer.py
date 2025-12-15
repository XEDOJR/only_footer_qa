from playwright.sync_api import sync_playwright

def test_footer_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://only.digital/", timeout=60000)

        # Ждём футер
        footer = page.locator("footer")
        footer.wait_for(state="visible", timeout=20000)  # увеличиваем таймаут

        # Проверяем наличие любого img внутри футера
        footer_images = footer.locator("img")
        if footer_images.count() == 0:
            # Альтернатива: проверяем фон через CSS
            background = footer.evaluate("el => getComputedStyle(el).backgroundImage")
            assert "url(" in background, "Логотип в футере не найден"
        else:
            assert footer_images.count() > 0, "Логотип в футере не найден"

        browser.close()
