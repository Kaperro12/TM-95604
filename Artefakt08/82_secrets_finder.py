import os
import re


def find_secrets(strings_path="../Artefakt02/decompiled_apk/res/values/strings.xml"):
    """
    Skaner inżynierski: wykorzystuje wyrażenia regularne (RegEx) do wykrywania
    wrażliwych danych zaszytych w zasobach aplikacji.
    """

    print(f">>> SKANOWANIE ZASOBÓW: {strings_path} <<<")

    if not os.path.exists(strings_path):
        print(f"BŁĄD: Nie odnaleziono pliku zasobów: {strings_path}")
        return

    with open(strings_path, "r", encoding="utf-8") as f:
        content = f.read()

    patterns = {
        "IP_Address": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
        "URL_Endpoint": r"https?://[^\s<>\"']+|www\.[^\s<>\"']+",
        "Potential_Secret": r"(?i)key|token|secret|password|auth|api_key",
        "API_Key_Format": r"[a-zA-Z0-9_-]{20,}"
    }

    results = []

    for label, pattern in patterns.items():
        matches = re.findall(pattern, content)

        for match in set(matches):
            if len(match) > 3 and not match.endswith(".xml"):
                results.append(f"[{label}] -> {match}")

    output_file = "82_secrets_found.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        if results:
            f.write("\n".join(results))
        else:
            f.write("Brak potencjalnych sekretów w strings.xml")

    print(f"[INFO] Liczba znalezionych potencjalnych sekretów: {len(results)}")
    print(f"[SUCCESS] Wynik zapisano do: {output_file}")

    if results:
        print("\n--- PRZYKŁADOWE ZNALEZISKA ---")
        for item in results[:10]:
            print(item)


if __name__ == "__main__":
    find_secrets()