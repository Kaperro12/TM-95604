import xml.etree.ElementTree as ET

ANDROID_NS = '{http://schemas.android.com/apk/res/android}'

manifest_path = "Artefakt02/decompiled_apk/AndroidManifest.xml"
output_path = "Artefakt05/52_inspection.log"

tree = ET.parse(manifest_path)
root = tree.getroot()

package_name = root.attrib.get("package", "BRAK")

permissions = []
for elem in root.findall("uses-permission"):
    perm = elem.attrib.get(f"{ANDROID_NS}name")
    if perm:
        permissions.append(perm)

activities = []
for elem in root.findall(".//activity"):
    activity_name = elem.attrib.get(f"{ANDROID_NS}name")
    if activity_name:
        activities.append(activity_name)

report_lines = []
report_lines.append("=== ARTEFAKT 5.2: RAPORT ANALIZY STATYCZNEJ ===")
report_lines.append("")
report_lines.append(f"Pakiet główny: {package_name}")
report_lines.append(f"Liczba aktywności: {len(activities)}")
report_lines.append("")

report_lines.append("Kluczowe uprawnienia (co aplikacja chce robić):")
if permissions:
    for perm in permissions:
        report_lines.append(f"- {perm}")
else:
    report_lines.append("- Brak uprawnień")

report_lines.append("")
report_lines.append("Przykładowe aktywności:")
if activities:
    for act in activities[:10]:
        report_lines.append(f"- {act}")
else:
    report_lines.append("- Brak aktywności")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("\n=== ARTEFAKT 5.2: RAPORT ANALIZY STATYCZNEJ ===")
print(f"Pakiet główny: {package_name}")
print(f"Liczba aktywności: {len(activities)}")
print("\nKluczowe uprawnienia (co aplikacja chce robić):")

if permissions:
    for perm in permissions:
        print(f"- {perm}")
else:
    print("- Brak uprawnień")

print(f"\n[OK] Sukces! Artefakt zapisany jako: {output_path}")