import xml.etree.ElementTree as ET
import glob
import json


def analyze_accessibility(path):
    gaps = []
    ns = '{http://schemas.android.com/apk/res/android}'

    files = glob.glob(path + "/**/*.xml", recursive=True)

    for file in files:
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                node_text = elem.get(f'{ns}text')
                node_desc = elem.get(f'{ns}contentDescription')
                node_id = elem.get(f'{ns}id', 'no-id')

                # Luka: jest tekst, ale nie ma opisu (contentDescription)
                if node_text and not node_desc:
                    gaps.append({
                        "file": file.split('/')[-1],
                        "id": node_id.split('/')[-1],
                        "text": node_text,
                        "issue": "Brak atrybutu contentDescription"
                    })
        except Exception:
            pass

    with open("Artefakt04/a11y_report.json", "w", encoding="utf-8") as f:
        json.dump(gaps, f, indent=4, ensure_ascii=False)

    print(f"Zapisano {len(gaps)} luk do Artefakt04/a11y_report.json")


analyze_accessibility("Artefakt02/decompiled_apk/res/layout")