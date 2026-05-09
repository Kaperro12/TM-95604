# 🏢 RAPORT Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS

**Data:** 09-05-2026  
**Audytor:** Kacper Radulak, nr albumu 95604 
**Projekt:** ApiDemos – statyczna analiza bezpieczeństwa APK

---

## 📊 1. OCENA KOŃCOWA (SECURITY SCORE)

**WYNIK:** 0/100  
**STATUS:** 🔴 REJECTED / NO-GO

Aplikacja nie powinna zostać dopuszczona do wydania produkcyjnego bez wykonania działań naprawczych.

---

## 🛡️ 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa (Zadanie 8.1)

**Problem:**  
W pliku `RiskyPermission.xml` wykryto aktywną flagę `debuggable=true` oraz ryzykowne uprawnienia systemowe.

**Wpływ:**  
Flaga debugowania umożliwia analizę działania aplikacji przez ADB i może ułatwić inżynierię wsteczną.  
Dodatkowo uprawnienia takie jak `INTERNET`, `CAMERA`, `RECORD_AUDIO`, `READ_CONTACTS` i `WRITE_EXTERNAL_STORAGE` zwiększają powierzchnię ataku.

---

### B. Wycieki Danych (Zadanie 8.2)

**Problem:**  
Skaner `82_secrets_finder.py` wykrył potencjalne sekrety, endpointy URL oraz frazy sugerujące obecność kluczy lub danych dostępowych.

**Wpływ:**  
W przypadku rzeczywistych sekretów możliwe byłoby ujawnienie adresów backendu, tokenów API lub danych konfiguracyjnych.  
Część znalezisk może być typu *False Positive*, dlatego wymagana jest ręczna analiza inżynierska.

---

### C. Biblioteki Zewnętrzne (Zadanie 8.3)

**Problem:**  
W pliku `requirements.txt` wykryto 4 podatne biblioteki, zapisane w `83_vulnerabilities.json`, w tym jedną o poziomie `CRITICAL`.

**Wpływ:**  
Największe zagrożenie stanowi podatność krytyczna w bibliotece `org.apache.commons:1.0.0`, która w symulacji została sklasyfikowana jako RCE.  
Podatne biblioteki zwiększają ryzyko ataków na łańcuch dostaw oprogramowania.

---

## 📝 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION)

1. **[PRIORYTET 1] Wyłączyć debugowanie aplikacji**
   - Ustawić `android:debuggable="false"` w konfiguracji produkcyjnej.

2. **[PRIORYTET 1] Zaktualizować podatne biblioteki**
   - Zastąpić stare wersje bibliotek aktualnymi wersjami bez znanych podatności CVE.

3. **[PRIORYTET 2] Ograniczyć uprawnienia aplikacji**
   - Usunąć wszystkie uprawnienia, które nie są wymagane przez funkcje biznesowe aplikacji.

4. **[PRIORYTET 2] Zweryfikować potencjalne sekrety**
   - Przenieść klucze API, tokeny i hasła poza kod oraz zasoby aplikacji.
   - Użyć bezpiecznych mechanizmów przechowywania, np. Keystore, Vault lub zmiennych środowiskowych.

5. **[PRIORYTET 3] Dodać automatyczny audyt do CI/CD**
   - Wdrożyć skanowanie manifestu, bibliotek i sekretów w GitHub Actions lub Jenkins.

---

## 🎓 WNIOSKI KOŃCOWE

Przeprowadzona statyczna analiza bezpieczeństwa wykazała kilka istotnych problemów:

- aplikacja działa z aktywną flagą `debuggable=true`,
- posiada ryzykowne uprawnienia systemowe,
- zawiera potencjalne sekrety lub dane wymagające ręcznej weryfikacji,
- korzysta z podatnych bibliotek zewnętrznych.

Końcowy wynik **0/100** oznacza, że aplikacja wymaga natychmiastowych poprawek bezpieczeństwa przed ewentualnym wdrożeniem produkcyjnym.

**Decyzja końcowa:** 🔴 **NO-GO / REJECTED**