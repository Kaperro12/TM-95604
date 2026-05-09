import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Artefakt06"))

from MainPage import MainPage


class GestureAutomator(MainPage):
    """
    MODUŁ GESTÓW (Layer 4): Rozszerzenie Page Objectu o fizykę dotyku.
    """

    def __init__(self):
        super().__init__()

    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):
        """
        Symulacja gestu SCROLL DOWN (procentowo).
        """

        print(f"[GESTURE] Start Swipe: Y={start_y} -> End Y={end_y} (t={duration_ms}ms)")

        if duration_ms < 200:
            return "BŁĄD: Gest zbyt szybki - grozi brakiem reakcji UI (Flick)."

        return f"SUKCES: Przewinięto listę o {int((start_y - end_y) * 100)}% wysokości ekranu."

    def long_press_element(self, element_key):
        """
        Symulacja Long Press na Resource ID.
        """

        # find_id dziedziczymy z BasePage przez MainPage
        selector = self.get_selector(element_key)

        if selector:
            return f"SUKCES: Wykonano LONG PRESS (2s) na elemencie: {selector}"

        return f"BŁĄD: Nie odnaleziono elementu {element_key} w mapie selektorów."


if __name__ == "__main__":
    print(">>> ZADANIE 7.1: TESTY FIZYKI DOTYKU <<<")
    print("-----------------------------------------")

    automator = GestureAutomator()

    result1 = automator.scroll_down_logic(start_y=0.8, end_y=0.2, duration_ms=800)
    print(result1)

    result2 = automator.long_press_element("ADD")
    print(result2)