from playwright.sync_api import sync_playwright

def test_footer_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Открываем страницу
        page.goto("https://only.digital/", timeout=60000)

        # Проверка наличия футера
        footer = page.locator("footer")
        assert footer.is_visible(), "Футер не отображается на странице"

        # Проверка логотипа в футере
        footer_logo = footer.locator("img")
        assert footer_logo.count() > 0, "Логотип в футере не найден"

        # Проверка ссылки на политику конфиденциальности
        privacy_link = footer.get_by_text("Privacy", exact=False)
        assert privacy_link.is_visible(), "Ссылка Privacy Policy не найдена"

        # Проверка наличия социальных ссылок
        social_links = footer.locator("a[href*='telegram'], a[href*='behance'], a[href*='vk'], a[href*='dribbble']")
        assert social_links.count() > 0, "Социальные ссылки в футере не найдены"

        browser.close()
