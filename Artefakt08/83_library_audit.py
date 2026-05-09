import json

requirements_path = "requirements.txt"
output_path = "83_vulnerabilities.json"

cve_database = {
    "com.google.android.gms:10.0.1": {
        "severity": "HIGH",
        "cve": "CVE-2016-2402",
        "description": "Stara wersja Google Play Services może zawierać znane podatności bezpieczeństwa."
    },
    "com.squareup.okhttp:2.7.5": {
        "severity": "MEDIUM",
        "cve": "CVE-2021-0341",
        "description": "Przestarzała biblioteka HTTP może zwiększać ryzyko problemów z komunikacją sieciową."
    },
    "org.apache.commons:1.0.0": {
        "severity": "CRITICAL",
        "cve": "CVE-2022-42889",
        "description": "Symulowana podatność typu RCE w bibliotece Apache Commons."
    },
    "com.android.support:25.0.0": {
        "severity": "LOW",
        "cve": "CVE-2017-13156",
        "description": "Stara wersja Android Support Library może zawierać znane problemy zgodności i bezpieczeństwa."
    }
}

print(">>> ZADANIE 8.3: ANALIZA ŁAŃCUCHA DOSTAW SCA <<<")

with open(requirements_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

libraries = [
    line.strip()
    for line in lines
    if line.strip() and not line.strip().startswith("#")
]

findings = []

for lib in libraries:
    if lib in cve_database:
        item = {
            "library": lib,
            "severity": cve_database[lib]["severity"],
            "cve": cve_database[lib]["cve"],
            "description": cve_database[lib]["description"]
        }
        findings.append(item)

        print(f"[{item['severity']}] {item['library']} -> {item['cve']}")
        print(f"Opis: {item['description']}")
        print("-" * 60)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(findings, f, indent=4, ensure_ascii=False)

print(f"[SUCCESS] Wykryto {len(findings)} podatności.")
print(f"[SUCCESS] Wygenerowano plik: {output_path}")