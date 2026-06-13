import requests


def test_api_connectivity():
    print(">>> ZADANIE 9.1: TEST POŁĄCZENIA Z API BACKENDOWYM <<<")

    # Adres testowego API, które symuluje backend aplikacji mobilnej
    base_url = "https://jsonplaceholder.typicode.com/todos/1"

    # Przykładowe nagłówki i token testowy
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mobile-QA-Tester",
        "Authorization": "Bearer test-token"
    }

    try:
        # Wykonanie żądania GET
        response = requests.get(base_url, headers=headers, timeout=5)

        # Analiza odpowiedzi
        status_code = response.status_code
        data = response.json()

        print(f"[DEBUG] Endpoint: {base_url}")
        print(f"[DEBUG] Status Code: {status_code}")
        print(f"[DEBUG] Response Body: {data}")

        # Asercja / logika testu
        if status_code == 200:
            print(f"[SUCCESS] API jest dostępne. Tytuł zadania: {data['title']}")
        else:
            print(f"[ERROR] Serwer zwrócił błąd: {status_code}")

    except Exception as e:
        print(f"[FATAL] Brak łączności z API: {e}")


if __name__ == "__main__":
    test_api_connectivity()