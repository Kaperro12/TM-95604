import xml.etree.ElementTree as ET

# Ścieżka do manifestu z Artefaktu02
manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"

print(f">>> URUCHAMIANIE AUDYTU: {manifest_path} <<<")

tree = ET.parse(manifest_path)
root = tree.getroot()

android_ns = "{http://schemas.android.com/apk/res/android}"

# Lista niebezpiecznych uprawnień
dangerous_list = [
    "READ_CONTACTS",
    "WRITE_EXTERNAL_STORAGE",
    "ACCESS_FINE_LOCATION",
    "INTERNET",
    "CAMERA",
    "RECORD_AUDIO"
]

risky_permissions = []

# Szukanie uprawnień
for perm in root.findall("uses-permission"):
    name = perm.get(android_ns + "name")

    if name:
        short_name = name.split(".")[-1]

        if short_name in dangerous_list:
            risky_permissions.append(name)

# Sprawdzenie flagi debuggable
application = root.find("application")

debuggable = "false"

if application is not None:
    debug_value = application.get(android_ns + "debuggable")

    if debug_value == "true":
        debuggable = "true"

# Generowanie XML
report = ET.Element(
    "SecurityAudit",
    app="ApiDemos_Security_Check",
    status="ReviewRequired"
)

flags = ET.SubElement(report, "Flags")
debug_node = ET.SubElement(flags, "Debuggable")
debug_node.text = debuggable

risk_node = ET.SubElement(report, "RiskyPermissions")

for perm in risky_permissions:
    p = ET.SubElement(risk_node, "Permission")
    p.text = perm

tree_out = ET.ElementTree(report)

tree_out.write(
    "RiskyPermission.xml",
    encoding="utf-8",
    xml_declaration=True
)

print(f"[INFO] Znaleziono {len(risky_permissions)} podejrzanych uprawnień.")

if debuggable == "true":
    print("[ALERT] Wykryto aktywną flagę DEBUGGABLE!")
else:
    print("[OK] Flaga debuggable wyłączona.")

print("[SUCCESS] Wygenerowano raport: RiskyPermission.xml")