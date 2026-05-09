# 🛡️ RAPORT ANALIZY UPRAWNIEŃ (PERMISSIONS RISK)

## 📄 1. Zawartość RiskyPermission.xml

Zidentyfikowano następujące wpisy krytyczne:

- **Debuggable:** `true`  
⚠️ **WYSOKIE RYZYKO** – aplikacja podatna na inżynierię wsteczną oraz debugowanie w czasie rzeczywistym.

- **Permissions:** Wykryto uprawnienia umożliwiające:
  - dostęp do Internetu (`INTERNET`)
  - zapis do pamięci zewnętrznej (`WRITE_EXTERNAL_STORAGE`)
  - dostęp do kontaktów (`READ_CONTACTS`)
  - dostęp do mikrofonu (`RECORD_AUDIO`)
  - dostęp do kamery (`CAMERA`)

---

## 🧠 2. Interpretacja Inżynierska

Najpoważniejszym problemem bezpieczeństwa jest aktywna flaga `debuggable="true"`.

Pozwala ona na wykorzystanie narzędzi ADB (`adb jdwp`) do śledzenia procesów aplikacji, podłączania debuggera oraz analizy działania aplikacji przez osoby niepowołane.

Dodatkowo aplikacja posiada wiele uprawnień wysokiego ryzyka. W przypadku przejęcia aplikacji przez złośliwe oprogramowanie możliwe byłoby:

- nagrywanie dźwięku,
- wykonywanie zdjęć,
- odczyt kontaktów,
- przesyłanie danych przez Internet,
- zapis plików poza sandboxem aplikacji.

Tak szeroki zakres uprawnień zwiększa powierzchnię potencjalnego ataku.

---

## 🔧 3. Akcja Korygująca

Zaleca się:

1. Wyłączenie flagi:

```xml
android:debuggable="false"
```

2. Ograniczenie liczby uprawnień wyłącznie do tych wymaganych biznesowo.

3. Dodanie automatycznej kontroli bezpieczeństwa w pipeline CI/CD
(GitHub Actions / Jenkins), która będzie blokować buildy zawierające:
- `debuggable="true"`
- nadmiarowe uprawnienia
- eksportowane komponenty bez zabezpieczeń.

---

## 📌 Wnioski Końcowe

Aplikacja wymaga dodatkowego utwardzenia bezpieczeństwa przed wdrożeniem produkcyjnym.

Największe ryzyko stanowi możliwość debugowania aplikacji oraz szeroki zakres przyznanych uprawnień systemowych.

---

**Raport wykonał:**  
Kacper Radulak  
Nr albumu: 95604  
Data: 09-05-2026