import xml.etree.ElementTree as ET
import os
import json

layout_dir = "Artefakt02/decompiled_apk/res/layout"
output_file = "Artefakt05/53_selectors.json"

ui_map = {
    "selectors": {}
}

# Iterujemy po plikach layoutów
for file_name in os.listdir(layout_dir):
    if file_name.endswith(".xml"):
        try:
            tree = ET.parse(os.path.join(layout_dir, file_name))
            root = tree.getroot()

            # Szukamy wszystkich elementów z atrybutem id
            for element in root.iter():
                res_id = element.attrib.get('{http://schemas.android.com/apk/res/android}id')
                if res_id:
                    # Oczyszczamy ID (np. @id/button -> button)
                    clean_id = res_id.split('/')[-1]

                    # Tworzymy nazwę biznesową (np. LOGIN_BTN)
                    business_name = clean_id.upper()

                    ui_map["selectors"][business_name] = clean_id
        except Exception:
            continue

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(ui_map, f, indent=4, ensure_ascii=False)

print(f"Zmapowano {len(ui_map['selectors'])} unikalnych elementów UI")
print(f"Zapisano do: {output_file}")