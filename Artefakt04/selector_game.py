import xml.etree.ElementTree as ET
import glob


def run_game():
    print("=== INTERAKTYWNY KREATOR SELEKTORÓW ===")

    target_id = input("1. Podaj wartość 'id' z raportu (np. lunch): ").strip()
    target_tag = input("2. Podaj wartość 'tag' z raportu (np. RadioButton): ").strip()

    matches = 0
    ns = '{http://schemas.android.com/apk/res/android}'

    # Przeszukujemy layouty z Artefakt02
    path = "Artefakt02/decompiled_apk/res/layout/*.xml"
    files = glob.glob(path)

    for file in files:
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                node_id = elem.get(f'{ns}id', '')
                node_tag = elem.tag

                # Warunek unikalności: ID musi zawierać wpisaną frazę, a TAG musi być identyczny
                if target_id in node_id and target_tag == node_tag:
                    matches += 1
        except Exception:
            continue

    print(f"\nWynik wyszukiwania: Znaleziono {matches} dopasowań.")

    with open("Artefakt04/xpath_verification.txt", "w", encoding="utf-8") as f:
        if matches == 1:
            print(">>> STATUS: ZALICZONE! Twój selektor jest unikalny. <<<")
            f.write(
                f"PROJEKT SELEKTORA:\n"
                f"ID: {target_id}\n"
                f"TAG: {target_tag}\n"
                f"STATUS: ZALICZONE\n"
                f"WYNIK: Znaleziono 1 dopasowanie"
            )
        else:
            print(">>> STATUS: BŁĄD! Musisz znaleźć unikalną parę ID + TAG (Wynik musi wynosić 1). <<<")
            f.write(
                f"PROJEKT SELEKTORA:\n"
                f"ID: {target_id}\n"
                f"TAG: {target_tag}\n"
                f"STATUS: BŁĄD\n"
                f"WYNIK: Znaleziono {matches} dopasowań"
            )


if __name__ == "__main__":
    run_game()