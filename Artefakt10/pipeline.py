import os
import subprocess
import shutil


def run_command(command, cwd=None, allow_fail=False):
    print(f"\n[PIPELINE] Uruchamiam: {command}")

    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
        text=True
    )

    if result.returncode != 0 and not allow_fail:
        raise RuntimeError(f"Błąd podczas wykonywania: {command}")

    return result.returncode


def main():
    print("=== ZADANIE 10.4: CLEAN-UP PIPELINE ===")

    project_root = os.path.abspath("..")
    artifact03_path = os.path.join(project_root, "Artefakt03")

    print(f"[INFO] Project root: {project_root}")
    print(f"[INFO] Artefakt03 path: {artifact03_path}")

    # 1. Sprzątanie starych wyników
    print("\n[KROK 1] Czyszczenie starych raportów...")
    shutil.rmtree("allure-results", ignore_errors=True)
    shutil.rmtree("allure-report", ignore_errors=True)
    os.makedirs("allure-results", exist_ok=True)
    print("[OK] Stare raporty usunięte.")

    # 2. Start infrastruktury Appium
    print("\n[KROK 2] Uruchamianie infrastruktury Docker/Appium...")
    run_command("docker compose up -d", cwd=artifact03_path)
    print("[OK] Infrastruktura uruchomiona.")

    # 3. Uruchomienie testów Pytest + Allure
    print("\n[KROK 3] Uruchamianie testów Pytest...")
    run_command(
        "pytest test_101_allure_init.py test_102_meta_reporting.py test_103_attachments.py --alluredir=allure-results",
        allow_fail=True
    )
    print("[OK] Testy wykonane. Wyniki zapisane w allure-results.")

    # 4. Dodanie informacji o środowisku
    print("\n[KROK 4] Dodawanie environment.properties...")
    with open("allure-results/environment.properties", "w", encoding="utf-8") as f:
        f.write("Feature=10.4: Clean-up Pipeline\n")
        f.write("OS=macOS\n")
        f.write("Project=TestowanieMobilne\n")
        f.write("Artifact=10\n")
        f.write("Tool=Pytest + Allure + Docker\n")
    print("[OK] Environment zapisany.")

    # 5. Generowanie statycznego raportu HTML
    print("\n[KROK 5] Generowanie raportu Allure HTML...")
    run_command("allure generate allure-results -o allure-report --clean")
    print("[OK] Raport wygenerowany w folderze allure-report.")

    # 6. Sprzątanie infrastruktury
    print("\n[KROK 6] Zatrzymywanie kontenerów Docker...")
    run_command("docker compose down", cwd=artifact03_path, allow_fail=True)
    print("[OK] Kontenery zatrzymane.")

    print("\n=== PIPELINE ZAKOŃCZONY POPRAWNIE ===")
    print("Raport HTML: Artefakt10/allure-report/index.html")


if __name__ == "__main__":
    main()