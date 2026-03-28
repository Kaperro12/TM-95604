import xml.etree.ElementTree as ET
import glob
import json
from collections import Counter


def analyze_stability(path):
    class_counts = Counter()
    total_elements = 0

    for file in glob.glob(path + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                class_counts[elem.tag] += 1
                total_elements += 1
        except Exception:
            pass

    # Obliczanie statystyk i werdyktu
    report = {
        "metrics": {},
        "verdict": "LOW_RISK",
        "warnings": []
    }

    threshold = 0.5  # 50% – próg krytyczny dla jednej klasy

    for cls, count in class_counts.items():
        percentage = round((count / total_elements) * 100, 2)
        report["metrics"][cls] = f"{percentage}% ({count} objects)"

        if percentage > (threshold * 100):
            report["verdict"] = "HIGH_RISK"
            report["warnings"].append(
                f"Class '{cls}' dominates UI ({percentage}%). Avoid By.className!"
            )

    with open("Artefakt04/stability_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print(f"Audit Complete. Verdict: {report['verdict']}")


analyze_stability("Artefakt02/decompiled_apk/res/layout")