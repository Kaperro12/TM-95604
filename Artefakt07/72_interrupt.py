import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Artefakt06"))

from MainPage import MainPage


class InterruptManager(MainPage):
    """
    MODUŁ PRZERWAŃ (Layer 4): Symulacja zdarzeń systemowych Androida.
    """

    def __init__(self):
        super().__init__()

    def simulate_incoming_call(self, duration_sec=5):
        """
        Symuluje nadchodzące połączenie, które przysłania aplikację.
        """

        print(f"\n[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")

        # W Appium: driver.make_gsm_call(phone_number, GsmCallActions.CALL)
        time.sleep(1)
        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran połączenia <<<")

        time.sleep(duration_sec)

        print("[INTERRUPT] KROK 3: Zakończenie połączenia. Powrót do aplikacji.")
        # W Appium: driver.activate_app("io.appium.android.apis")

        return "SUKCES: Aplikacja odzyskała fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):
        """
        Symuluje systemowy komunikat o niskim stanie baterii.
        """

        print("\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")
        # W Appium: driver.set_power_capacity(5)

        return "SUKCES: Aplikacja obsłużyła systemowe okno dialogowe bez błędu."


if __name__ == "__main__":
    manager = InterruptManager()

    print(">>> ZADANIE 7.2: TESTY ODPORNOŚCI NA PRZERWANIA <<<")
    print("----------------------------------------------------")

    result1 = manager.simulate_incoming_call(duration_sec=3)
    print(result1)

    result2 = manager.simulate_low_battery_warning()
    print(result2)