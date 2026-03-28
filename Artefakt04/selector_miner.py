import xml.etree.ElementTree as ET
import glob
import json
import os

results = []

path = "Artefakt02/decompiled_apk/res/layout"
files = glob.glob(path + "/**/*.xml", recursive=True)

for file in files:
    try:
        tree = ET.parse(file)
        for elem in tree.iter():
            res_id = elem.get('{http://schemas.android.com/apk/res/android}id')
            if res_id:
                clean_id = res_id.split('/')[-1]
                results.append({
                    "file": os.path.basename(file),
                    "id": clean_id,
                    "tag": elem.tag
                })
    except Exception:
        pass  # pomijamy błędy bez spamowania w terminalu

# zapis do JSON
with open("Artefakt04/miner_report.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

# tylko jedno podsumowanie
print(f"Zapisano {len(results)} rekordów do Artefakt04/miner_report.json")