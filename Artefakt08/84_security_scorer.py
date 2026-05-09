import os
import json
import xml.etree.ElementTree as ET

score = 100
deductions = []

# 1. ANALIZA FLAG Z XML (Zadanie 8.1)
xml_path = "RiskyPermission.xml"

if os.path.exists(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    debuggable_node = root.find(".//Debuggable")
    debuggable = debuggable_node.text if debuggable_node is not None else "false"

    if debuggable == "true":
        score -= 30
        deductions.append("[-30] Flaga Debuggable jest AKTYWNA (High Risk)")

    risky_permissions = root.findall(".//Permission")
    if risky_permissions:
        deduction = len(risky_permissions) * 5
        score -= deduction
        deductions.append(
            f"[-{deduction}] Wykryto {len(risky_permissions)} ryzykownych uprawnień (Low Risk)"
        )
else:
    deductions.append("[INFO] Brak pliku RiskyPermission.xml - pominięto analizę uprawnień")

# 2. ANALIZA PODATNOŚCI Z JSON (Zadanie 8.3)
json_path = "83_vulnerabilities.json"

if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        vulnerabilities = json.load(f)

    for v in vulnerabilities:
        severity = v.get("severity", "").upper()
        library = v.get("library", "unknown")

        if severity == "CRITICAL":
            score -= 40
            deductions.append(f"[-40] Krytyczna luka w {library} (Critical)")
        elif severity == "HIGH":
            score -= 20
            deductions.append(f"[-20] Poważna luka w {library} (High)")
        elif severity == "MEDIUM":
            score -= 10
            deductions.append(f"[-10] Średnia luka w {library} (Medium)")
        elif severity == "LOW":
            score -= 5
            deductions.append(f"[-5] Niska luka w {library} (Low)")
else:
    deductions.append("[INFO] Brak pliku 83_vulnerabilities.json - pominięto analizę bibliotek")

# Nie pozwalamy zejść poniżej 0
score = max(score, 0)

if score >= 80:
    status = "APPROVED"
elif score >= 50:
    status = "NEEDS FIX"
else:
    status = "REJECTED"

report_lines = []
report_lines.append(">>> ZADANIE 8.4: OBLICZANIE SECURITY SCORE <<<")
report_lines.append("")
report_lines.append(f"[WYNIK KOŃCOWY]: {score}/100")
report_lines.append(f"[STATUS]: {status}")
report_lines.append("")
report_lines.append("Potrącenia punktów:")

for item in deductions:
    report_lines.append(f"- {item}")

with open("84_risk_score.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("\n".join(report_lines))
print("\n[SUCCESS] Raport zapisano do: 84_risk_score.txt")