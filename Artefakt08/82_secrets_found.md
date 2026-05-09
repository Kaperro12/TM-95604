# 🛡️ RAPORT ANALIZY WYCIEKÓW (SECRETS)

**Student:** Kacper Radulak  
**Indeks:** 95604  
**Data raportu:** 09-05-2026

---

# 🛑 1. Trzy najbardziej groźne znaleziska (High Risk)

Poniższe elementy wymagają natychmiastowej analizy bezpieczeństwa:

## 1. [Potential_Secret] -> password

- **Uzasadnienie:**  
Występowanie słowa `password` w plikach zasobów aplikacji może sugerować obecność domyślnego hasła, mechanizmu autoryzacji lub testowych danych logowania pozostawionych przez programistów.

---

## 2. [Potential_Secret] -> api_key

- **Uzasadnienie:**  
Fraza `api_key` bardzo często oznacza klucz dostępu do usług backendowych lub API zewnętrznych. Wycieki takich danych mogą umożliwić nieautoryzowany dostęp do infrastruktury aplikacji.

---

## 3. [URL_Endpoint] -> http://...

- **Uzasadnienie:**  
Wykryte endpointy URL mogą ujawniać adresy serwerów testowych, API lub usług backendowych wykorzystywanych przez aplikację. Informacje takie pomagają atakującemu mapować architekturę systemu.

---

# 🟢 2. Trzy znaleziska typu "False Positive" (Low/No Risk)

Poniższe elementy zostały błędnie oznaczone jako potencjalne zagrożenie:

## 1. [URL_Endpoint] -> http://www.google.com

- **Uzasadnienie:**  
Jest to standardowy adres używany do testów połączenia internetowego lub przykładowych odwołań dokumentacyjnych.

---

## 2. [API_Key_Format] -> abc_font_family_display_3_material

- **Uzasadnienie:**  
To standardowy identyfikator zasobu biblioteki Material Design, a nie rzeczywisty sekret lub token dostępu.

---

## 3. [API_Key_Format] -> table_layout_1_triple_star

- **Uzasadnienie:**  
Element pasuje do wzorca długiego ciągu znaków, jednak jest jedynie nazwą zasobu interfejsu użytkownika.

---

# 📌 Wnioski końcowe

Automatyczne skanowanie RegEx skutecznie identyfikuje potencjalne wycieki danych, jednak wymaga dodatkowej analizy inżynierskiej.

Największym problemem tego typu skanerów jest brak rozumienia kontekstu biznesowego aplikacji, co prowadzi do występowania tzw. *False Positives*.

W praktyce każdy wykryty sekret powinien zostać:
- ręcznie zweryfikowany,
- sprawdzony pod kątem wykorzystania w kodzie,
- przeniesiony do bezpiecznych mechanizmów przechowywania (np. Vault, zmienne środowiskowe, Keystore).

---

**Raport wykonał:**  
Kacper Radulak