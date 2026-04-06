import xml.etree.ElementTree as ET
import json
import os

def extract_caps():
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    ns = {'android': 'http://schemas.android.com/apk/res/android'}

    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()

        package = root.attrib.get('package')

        main_activity = ""
        for activity in root.findall(".//activity"):
            intent_filters = activity.findall("intent-filter")
            for intent in intent_filters:
                action = intent.find(".//action[@android:name='android.intent.action.MAIN']", ns)
                category = intent.find(".//category[@android:name='android.intent.category.LAUNCHER']", ns)
                if action is not None and category is not None:
                    main_activity = activity.get(f"{{{ns['android']}}}name")
                    break
            if main_activity:
                break

        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "appPackage": package,
            "appActivity": main_activity,
            "deviceName": "emulator-5554",
            "noReset": True
        }

        with open("51_caps.json", "w", encoding="utf-8") as f:
            json.dump(capabilities, f, indent=4)

        print(f"Sukces! Wykryto: {package} / {main_activity}")

    except Exception as e:
        print(f"Błąd czytania manifestu: {e}. Czy ścieżka do Artefakt02 jest poprawna?")

if __name__ == "__main__":
    extract_caps()