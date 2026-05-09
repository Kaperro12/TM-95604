import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Artefakt06"))

from MainPage import MainPage


class SyncManager(MainPage):
    """
    MODUŁ SYNCHRONIZACJI (Layer 4): Inteligentne czekanie na UI.
    """

    def __init__(self):
        super().__init__()

    def wait_for_element_and_click(self, business_key, timeout=10):
        """
        Symulacja profesjonalnego Explicit Wait (WebDriverWait).
        """

        selector = self.get_selector(business_key)

        if not selector:
            return f"BŁĄD: Brak klucza '{business_key}' w mapie!"

        print(f"[SYNC] Rozpoczynam oczekiwanie na: {selector} (max {timeout}s)")

        # Symulacja pętli sprawdzającej obecność elementu (Polling)
        start_time = time.time()
        found = False

        # W rzeczywistym Appium:
        # element = WebDriverWait(driver, timeout).until(
        #     EC.presence_of_element_located(...)
        # )

        time.sleep(1.5)  # Symulacja opóźnienia ładowania aplikacji

        found = True

        end_time = time.time()
        duration = round(end_time - start_time, 2)

        if found:
            return (
                f"SUKCES: Element '{selector}' dostępny po {duration}s. "
                f"Wykonano CLICK."
            )

        return f"TIMEOUT: Element '{selector}' nie pojawił się w czasie {timeout}s."

    def simulate_timeout_case(self):
        """
        Symulacja timeoutu oczekiwania.
        """

        print("\n[SYNC] Test przypadku TIMEOUT")

        timeout = 3

        print(f"[SYNC] Oczekiwanie na nieistniejący element (max {timeout}s)")
        time.sleep(timeout)

        return "TIMEOUT: Element nie pojawił się w zadanym czasie."


if __name__ == "__main__":
    manager = SyncManager()

    print(">>> ZADANIE 7.4: SYNCHRONIZACJA I EXPLICIT WAITS <<<")
    print("------------------------------------------------------")

    result1 = manager.wait_for_element_and_click("ADD", timeout=5)
    print(result1)

    result2 = manager.simulate_timeout_case()
    print(result2)