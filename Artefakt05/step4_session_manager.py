import json

caps_path = "Artefakt05/51_caps.json"
selectors_path = "Artefakt05/53_selectors.json"
log_path = "Artefakt05/54_session.log"

# 1. Wczytywanie Capsów
with open(caps_path, "r", encoding="utf-8") as f:
    caps_data = json.load(f)

# 2. Wczytywanie Selektorów
with open(selectors_path, "r", encoding="utf-8") as f:
    ui_map = json.load(f)

# 3. Inteligentne pobieranie danych (obsługa różnych formatów JSON)
app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName") or "emulator-5554"

ui_elements_count = len(ui_map.get("selectors", {}))

# 4. Weryfikacja integracji
if not app_pkg or not app_act:
    status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
else:
    status_msg = "READY TO CONNECT"

report_lines = [
    "=== ZADANIE 5.4: INTEGRACJA ARTEFAKTÓW (STABLE BUILD) ===",
    "",
    f"Target App   : {app_pkg if app_pkg else 'BRAK'}",
    f"Main Activity: {app_act if app_act else 'BRAK'}",
    f"Device       : {dev_name}",
    f"UI Elements  : {ui_elements_count} loaded",
    f"Status       : {status_msg}"
]

with open(log_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("\n=== ZADANIE 5.4: SESSION READINESS REPORT ===")
print(f"Target App   : {app_pkg if app_pkg else 'BRAK'}")
print(f"Main Activity: {app_act if app_act else 'BRAK'}")
print(f"Device       : {dev_name}")
print(f"UI Elements  : {ui_elements_count} loaded")
print(f"Status       : {status_msg}")
print(f"\nLog zapisano do: {log_path}")