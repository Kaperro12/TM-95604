import json
import xml.etree.ElementTree as ET

caps_path = "Artefakt05/51_caps.json"
selectors_path = "Artefakt05/53_selectors.json"
result_path = "Artefakt05/55_result.xml"

# Wczytanie danych
with open(caps_path, "r", encoding="utf-8") as f:
    caps_data = json.load(f)

with open(selectors_path, "r", encoding="utf-8") as f:
    ui_map = json.load(f)

feedback_report = []

# Pobranie danych z caps
current_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")

# 1. Weryfikacja pakietu
if current_pkg == "io.appium.android.apis":
    feedback_report.append({
        "feature": "Identyfikacja Aplikacji",
        "status": "ZGODNY",
        "message": f"Pakiet {current_pkg} poprawnie zmapowany."
    })
else:
    feedback_report.append({
        "feature": "Identyfikacja Aplikacji",
        "status": "DO POPRAWY",
        "message": f"Niezgodność pakietu. Wykryto {current_pkg}, sprawdź konfigurację manifestu."
    })

# 2. Weryfikacja dostępności elementów
target_element = "ACCESSIBILITY"
selectors_dict = ui_map.get("selectors", {})

if target_element in selectors_dict:
    feedback_report.append({
        "feature": "Dostępność UI",
        "status": "ZGODNY",
        "message": f"Element {target_element} jest dostępny w layoutach."
    })
else:
    sample_keys = list(selectors_dict.keys())[:3]
    feedback_report.append({
        "feature": "Dostępność UI",
        "status": "INFORMACJA",
        "message": f"Nie odnaleziono ID '{target_element}'. Sugestia: zweryfikuj czy element nie zmienił nazwy na jedną z dostępnych: {sample_keys}."
    })

# Ustalenie końcowego wyniku testu
overall_pass = all(item["status"] == "ZGODNY" for item in feedback_report)

# Budowa XML
testsuite = ET.Element("testsuite", name="Artefakt05ConsistencyTest", tests=str(len(feedback_report)))

failures_count = 0
for item in feedback_report:
    testcase = ET.SubElement(testsuite, "testcase", name=item["feature"])

    if item["status"] != "ZGODNY":
        failures_count += 1
        failure = ET.SubElement(testcase, "failure", message=item["message"])
        failure.text = item["status"]
    else:
        system_out = ET.SubElement(testcase, "system-out")
        system_out.text = item["message"]

testsuite.set("failures", str(failures_count))

tree = ET.ElementTree(testsuite)
tree.write(result_path, encoding="utf-8", xml_declaration=True)

# Wynik w terminalu
print("=== ZADANIE 5.5: CONSISTENCY TEST ===")
for item in feedback_report:
    print(f"[{item['status']}] {item['feature']}: {item['message']}")

if overall_pass:
    print("[PASS] Blok 5 zakończony powodzeniem. Raport zapisano w 55_result.xml")
else:
    print("[FAIL] Blok 5 zakończony z ostrzeżeniami. Raport zapisano w 55_result.xml")