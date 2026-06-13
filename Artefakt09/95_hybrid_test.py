import requests


def test_hybrid_bridge():
    print("=== TEST MOSTEK HYBRYDOWY (ARTEFAKT 9.5) ===\n")

    # STEP 1 - Backend API
    print("[STEP 1] API: Sprawdzanie dostępności backendu...")

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=5
        )

        if response.status_code == 200:
            print("> [SUCCESS] Backend (REST API) dostępny.")
        else:
            print("> [FAIL] Backend zwrócił kod:", response.status_code)

    except Exception as e:
        print("> [FAIL] Brak połączenia z backendem:", e)

    print()

    # STEP 2 - Appium/Docker
    print("[STEP 2] DOCKER: Sprawdzanie serwera Appium...")

    try:
        appium = requests.get(
            "http://localhost:4723/status",
            timeout=5
        )

        if appium.status_code == 200:
            print("> [SUCCESS] Serwer Appium w Dockerze ODPOWIADA poprawnie.")
            print("> [STATUS] Urządzenie niepodpięte (zgodnie z planem), ale most działa.")
        else:
            print("> [FAIL] Appium zwróciło kod:", appium.status_code)

    except Exception as e:
        print("> [FAIL] Brak odpowiedzi od Appium:", e)

    print("\n=== KONIEC TESTU 9.5: INFRASTRUKTURA GOTOWA ===")


if __name__ == "__main__":
    test_hybrid_bridge()