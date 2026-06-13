import requests
from jsonschema import validate, ValidationError


def test_json_schema():
    print(">>> ZADANIE 9.3: WALIDACJA STRUKTURY JSON (KONTRAKT) <<<")

    url = "https://jsonplaceholder.typicode.com/posts/1"

    # DEFINICJA SCHEMATU
    # Określamy, że userId i id MUSZĄ być liczbami,
    # a title i body MUSZĄ być tekstami.
    expected_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title"]
    }

    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        data = response.json()

        print(f"[DEBUG] Endpoint: {url}")
        print(f"[DEBUG] Status Code: {status}")
        print(f"[DEBUG] Response Body: {data}")

        if status != 200:
            print(f"[FAIL] API zwróciło nieoczekiwany status: {status}")
            return

        validate(instance=data, schema=expected_schema)

        print("[SUCCESS] Kontrakt zachowany. Struktura JSON jest poprawna.")
        print(f"[DEBUG] Zweryfikowano pola dla obiektu ID: {data['id']}")
        print("[INFO] userId oraz id są liczbami, title oraz body są tekstami.")

    except ValidationError as e:
        print("[FAIL] Struktura JSON niezgodna ze schematem.")
        print(f"[DETAILS] {e.message}")

    except Exception as e:
        print(f"[FATAL] Błąd podczas walidacji API: {e}")


if __name__ == "__main__":
    test_json_schema()