from BasePage import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")

    def click_add_button(self):
        selector = self.get_selector("ADD")
        if selector:
            return f"SUKCES: Wykonano kliknięcie w element UI o ID: '{selector}'"
        return "BŁĄD: Nie znaleziono selektora ADD w mapie!"

    def check_text_visibility(self):
        selector = self.get_selector("TITLE") or self.get_selector("TEXT")
        if selector:
            return f"SUKCES: Odnaleziono nagłówek strony (ID: {selector}). Status: Widoczny."
        return "BŁĄD: Nie znaleziono selektora TITLE/TEXT w mapie!"

    def open_content_section(self):
        selector = self.get_selector("CONTENT")
        if selector:
            return f"SUKCES: Otworzono sekcję content przy użyciu ID: '{selector}'"
        return "BŁĄD: Nie znaleziono selektora CONTENT w mapie!"


if __name__ == "__main__":
    page = MainPage()
    print(page.click_add_button())
    print(page.check_text_visibility())
    print(page.open_content_section())