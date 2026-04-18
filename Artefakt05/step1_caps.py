import xml.etree.ElementTree as ET
import json

ANDROID_NS = '{http://schemas.android.com/apk/res/android}'

manifest_path = "Artefakt02/decompiled_apk/AndroidManifest.xml"
output_path = "Artefakt05/51_caps.json"

tree = ET.parse(manifest_path)
root = tree.getroot()

package_name = root.attrib.get("package")
launchable_activity = None

application = root.find("application")
if application is not None:
    for activity in application.findall("activity"):
        activity_name = activity.attrib.get(f"{ANDROID_NS}name")
        for intent_filter in activity.findall("intent-filter"):
            actions = [
                a.attrib.get(f"{ANDROID_NS}name")
                for a in intent_filter.findall("action")
            ]
            categories = [
                c.attrib.get(f"{ANDROID_NS}name")
                for c in intent_filter.findall("category")
            ]

            if "android.intent.action.MAIN" in actions and "android.intent.category.LAUNCHER" in categories:
                launchable_activity = activity_name
                break

        if launchable_activity:
            break

caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": package_name,
    "appium:appActivity": launchable_activity
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(caps, f, indent=4, ensure_ascii=False)

print(f"Sukces! Wykryto: {package_name} / {launchable_activity}")
print(f"Zapisano do: {output_path}")