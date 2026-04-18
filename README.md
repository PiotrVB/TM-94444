# 📱 Mobile Automation & Cloud-Ready Testing Suite
**Prowadzący:** mgr Mariusz Dworniczak  
**Student:** Piotr Benetkiewicz  
**Numer Albumu:** 94444

---

## 🏗️ Architektura Projektu (Marketing & Tech Stack)
Ten projekt to kompletny ekosystem testowy oparty na podejsciu **Cloud-Ready / Headless**. Zamiast polegać na ciężkich emulatorach, skupiamy się na narzędziach CLI, analizie statycznej, konteneryzacji (Docker) oraz automatyzacji procesów (Pipeline).

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
* **Co zrobiono:** Przygotowano strukturę projektu, skonfigurowano repozytorium GitHub, Dockerfile oraz środowisko do dalszych laboratoriów.
* **Wniosek:** Docker pozwala uruchamiać identyczne środowisko na różnych komputerach bez ręcznej instalacji wszystkich zależności lokalnie.

### 🔹 BLOK 2: Debugowanie i Analiza Statyczna (MobSF)
Zrozumienie "wnętrza" aplikacji mobilnej przed przystąpieniem do testów.
* **Co zrobiono:** Wykorzystano narzędzia do dekompilacji i analizy APK, sprawdzono manifest, permissions, API level, ABI i hash pliku.
* **Wniosek:** Analiza statyczna pozwala wykryć ryzyka i ważne informacje o aplikacji jeszcze przed uruchomieniem testów dynamicznych.

### 🔹 BLOK 3-4: Fundamenty Skryptowania (Python for QA)
Budowa logiki testowej w języku Python.
* **Co zrobiono:** Tworzono pierwsze skrypty pomocnicze, parsowano XML, analizowano layouty, selektory i strukturę aplikacji.
* **Wniosek:** Python pozwala automatyzować żmudne zadania analityczne i budować własne narzędzia QA.

### 🔹 BLOK 5-7: Hybrydowe Testowanie API (Requests & Pytest)
Weryfikacja warstwy backendowej aplikacji mobilnej.
* **Co zrobiono:** Testowano endpointy REST, wykonywano operacje GET i POST, walidowano JSON oraz sprawdzano błędy i integrację z Appium.
* **Wniosek:** Testowanie API pozwala wyłapać błędy zanim uruchomimy ciężkie testy UI.

### 🔹 BLOK 8: Appium UI Automation (Deep Dive)
Automatyzacja interakcji z interfejsem użytkownika.
* **Co zrobiono:** Wykonano audyt bezpieczeństwa aplikacji, analizę manifestu, wyszukiwanie sekretów, analizę bibliotek i scoring ryzyka.
* **Wniosek:** Tester mobilny powinien rozumieć nie tylko UI, ale też bezpieczeństwo aplikacji i zależności zewnętrzne.

### 🔹 BLOK 9: Konteneryzacja Serwera (Docker Compose)
Izolacja silnika Appium od systemu operacyjnego.
* **Co zrobiono:** Testowano API backendowe, sprawdzano CRUD, walidację schematu JSON, testy negatywne oraz hybrydowy most API + Appium.
* **Wniosek:** Połączenie API i Appium skraca czas testów i pozwala lepiej rozdzielić problemy backendu od problemów UI.

### 🔹 BLOK 10: MASTER PIPELINE (Capstone Project) 🏆
Finałowa automatyzacja całego procesu testowego.
* **Co zrobiono:** Stworzono testy raportowane przez Allure, załączniki błędów, pipeline uruchamiający testy i generujący raport oraz końcowe portfolio projektu.
* **Wniosek:** Automatyzacja pipeline pokazuje pełny przepływ pracy inżyniera testów – od uruchomienia środowiska po raport końcowy.

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
python pipeline.py

# Po zakończeniu zobacz raport
allure serve allure-results