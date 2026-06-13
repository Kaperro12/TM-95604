# 📱 Mobile Automation & Cloud-Ready Testing Suite
**Prowadzący:** mgr Mariusz Dworniczak  
**Student:** Kacper Radulak  
**Numer Albumu:** 95604

---

## 🏗️ Architektura Projektu (Marketing & Tech Stack)

Ten projekt to kompletny ekosystem testowy oparty na podejściu **Cloud-Ready / Headless**. Zamiast polegać na ciężkich emulatorach, skupiamy się na narzędziach CLI, analizie statycznej, konteneryzacji (Docker) oraz automatyzacji procesów (Pipeline).

**Główne technologie:**
* **Język:** Python 3.10+
* **Automatyzacja UI:** Appium 2.x (Mobile Engine)
* **Infrastruktura:** Docker & Docker Compose
* **Raportowanie:** Allure Framework
* **Analiza:** MobSF (Static Analysis) & ADB CLI

---

## 📅 PRZEBIEG LABORATORIUM (Kamienie Milowe)

### 🔹 BLOK 1: Tooling & Environment (Infrastruktura)

Przygotowanie bazy narzędziowej w modelu kontenerowym.

* **Co zrobiono:** Pobranie i konfiguracja obrazów `appium`, `android-sdk` oraz `mobsf`.
* **Wniosek:** Używamy obrazów Docker zamiast instalować wszystko lokalnie, bo każda instalacja manualna to źródło potencjalnych błędów – różne wersje Javy, Pythona czy SDK mogą powodować konflikty trudne do debugowania. Docker daje nam gotowe, odizolowane środowisko, które działa tak samo na każdym komputerze – moim laptopie, komputerze uczelni czy serwerze CI/CD. To podejście nazywa się "works on my machine" problem solved.

### 🔹 BLOK 2: Debugowanie i Analiza Statyczna (MobSF)

Zrozumienie "wnętrza" aplikacji mobilnej przed przystąpieniem do testów.

* **Co zrobiono:** Wykorzystanie MobSF do skanowania plików APK pod kątem podatności i uprawnień.
* **Wniosek:** Analiza statyczna APK daje testerowi wgląd w aplikację zanim jeszcze ją uruchomi. Można sprawdzić jakie uprawnienia systemowe żąda aplikacja (np. dostęp do mikrofonu, lokalizacji, kontaktów), czy plik nie zawiera zahardkodowanych haseł lub kluczy API, oraz czy nie ma składników z błędną konfiguracją bezpieczeństwa (np. `android:debuggable="true"`). To tańsze i szybsze niż szukanie tych samych problemów przez testy dynamiczne.

### 🔹 BLOK 3-4: Fundamenty Skryptowania (Python for QA)

Budowa logiki testowej w języku Python.

* **Co zrobiono:** Uczyłem się struktur danych używanych w testach – słowników do przechowywania danych testowych i capabilities Appium, list do grupowania przypadków testowych oraz funkcji do organizowania powtarzalnych kroków. Ćwiczyłem też obsługę wyjątków (`try/except`), która jest niezbędna gdy element UI nie zostanie znaleziony, oraz pracę z modułem `subprocess` do wywoływania komend ADB z poziomu Pythona.

### 🔹 BLOK 5-7: Hybrydowe Testowanie API (Requests & Pytest)

Weryfikacja warstwy backendowej aplikacji mobilnej.

* **Co zrobiono:** Testowanie endpointów REST (JSONPlaceholder), obsługa kodów HTTP i asercja danych JSON.
* **Wniosek:** Testowanie API pozwala wyłapać błędy zanim uruchomimy ciężkie testy UI.

### 🔹 BLOK 8: Appium UI Automation (Deep Dive)

Automatyzacja interakcji z interfejsem użytkownika.

* **Co zrobiono:** Korzystałem z selektorów `resource-id` (najstabilniejszy, gdy element ma unikalne ID), `xpath` (elastyczny, ale wolniejszy – używałem go gdy ID nie było dostępne) oraz `accessibility id` (dobry dla elementów z etykietą dostępności). Symulowałem typowe akcje użytkownika: kliknięcia przycisków, wpisywanie tekstu w pola formularzy, przewijanie listy (`swipe`), długie przytrzymanie elementu (`long press`) oraz obsługę przerwań takich jak przychodzące powiadomienia systemowe.

### 🔹 BLOK 9: Konteneryzacja Serwera (Docker Compose)

Izolacja silnika Appium od systemu operacyjnego.

* **Co zrobiono:** Stworzenie pliku `docker-compose.yml` zarządzającego serwerem Appium i sterownikami.

### 🔹 BLOK 10: MASTER PIPELINE (Capstone Project) 🏆

Finałowa automatyzacja całego procesu testowego.

* **Co zrobiono:** Stworzenie skryptu `pipeline.py`, który w jednym cyklu:
  1. Rezerwuje zasoby i stawia infrastrukturę Docker.
  2. Wykonuje testy hybrydowe (API + UI).
  3. Generuje profesjonalny raport Allure z metadanymi.
  4. Czyści środowisko po zakończonej pracy.

---

## 📊 Raportowanie Wyników (Allure)

Projekt wykorzystuje zaawansowane raportowanie Allure, które pozwala na:

* Śledzenie kroków testowych (`@allure.step`).
* Analizę błędów wraz z załącznikami (zrzuty ekranu, logi JSON).
* Dokumentowanie środowiska wykonawczego w sekcji **Environment**.

---

## 🚀 Jak uruchomić cały proces?

```bash
# Wejdź do folderu finałowego
cd Artefakt10

# Uruchom wszystko jednym poleceniem
python3 pipeline.py

# Po zakończeniu zobacz raport
allure serve allure-results
```
