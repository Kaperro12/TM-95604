import json
import os


class BasePage:
    def __init__(self, selectors_file="../Artefakt05/53_selectors.json"):
        with open(selectors_file, "r", encoding="utf-8") as f:
            self.selectors = json.load(f)["selectors"]

    def get_selector(self, business_name):
        return self.selectors.get(business_name, None)


if __name__ == "__main__":
    page = BasePage()
    print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(page.selectors)} elementów.")
    print(f"Weryfikacja klucza 'ADD': {page.get_selector('ADD')}")