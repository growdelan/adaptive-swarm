# Scenariusze regresyjne

Przypadki sprawdzają decyzje protokołu przy zadanej historii oraz etap eval na uruchamialnym kodzie. Są oddzielone od pakietu instalowanego skilla. Dane historyczne, oceny i pomiary w `cases.json` są syntetycznymi wejściami testu: nie stanowią dowodów, że rój osiągnął opisane korzyści w rzeczywistym projekcie.

## Odtworzenie

1. Z katalogu repozytorium wyświetl przypadki: `python3 benchmarks/prepare.py`.
2. Przygotuj przypadek w nowym folderze poza repozytorium, np. `python3 benchmarks/prepare.py first-confirmation /tmp/swarm-first-check`. Skrypt odmawia nadpisania istniejącego folderu. Kopiuje dokładny snapshot skilla, żądanie i dane wejściowe; nie kopiuje klucza odpowiedzi ani raportów.
3. Uruchom świeżą sesję Codex lub niezależnego subagenta z dostępem do tego folderu. Zleć: „Wykonaj REQUEST.md w tym folderze; pracuj tylko tutaj”. Do porównania wydań zachowuj model i effort; pierwsze testy używały `gpt-6-sol`, `medium`. Nie przekazuj wykonawcy oczekiwanego wyniku.
4. Po zakończeniu niezależnie sprawdź zmiany w plikach, nie tylko raport końcowy. [Klucz oceny](expectations.md) jest przeznaczony dla oceniającego. Zapisz wersję źródła, przypadek, model/effort, zaobserwowane działania, dowody i wynik PASS / FAIL / UNVERIFIED. Zmiana plików to dowód zapisu decyzji; deklaracja uruchomienia narzędzia nie dowodzi jego użycia.
5. Zachowaj raport i potrzebne artefakty przed usunięciem izolowanego folderu. Testy nie powinny publikować zmian ani korzystać z systemów produkcyjnych.

## Zakres i granice

Większość przypadków sprawdza poszczególne decyzje po dostarczonych ocenach. `eval-missed-defect` i `eval-correct-result` sprawdzają niezależnego ewaluatora na rzeczywistych wywołaniach małego modułu Pythona: wykonawca testu otrzymuje kontrakt, kod sprzed i po deklarowanej naprawie, test oraz raport implementacji. Zapisuje wyłącznie `EVALUATION.md`. Nie otrzymuje klucza odpowiedzi. Para obejmuje błędny i poprawny rezultat przy tym samym istniejącym teście; sam zielony wynik tego testu nie rozstrzyga kontraktu.

`recurring-defect-after-done` sprawdza rozważenie trwałego zabezpieczenia przy syntetycznej historii powtórzeń i zachowanie granic zamkniętego zadania. Nie sprawdza skuteczności samego zabezpieczenia.

`planning-shared-contract` i `planning-independent-results` izolują etap organizacji pracy. Agent otrzymuje wymagania oraz kod i zapisuje wyłącznie `PLAN.md`: zakresy odpowiedzialności, briefy, kolejność/równoległość i sposób integracji oraz eval. Pierwszy przypadek zawiera zależność API/UI mimo rozłącznych plików; drugi obejmuje dwie małe niezależne biblioteki. Nie wykonują implementacji i nie mierzą faktycznej jakości integracji ani czasu dostarczenia. Dopuszczają wykonanie małego zadania przez koordynatora, bez wymuszania dodatkowych ról.

Żaden z tych przypadków nie jest pełnym wykonaniem od celu do niezależnego eval. Wyłączenie powoływania agentów w żądaniu testowym izoluje odpowiedni etap i nie zmienia reguł zwykłego używania skilla. Ocena testowa jest wykonywana z zewnątrz.

Przypadki decyzji protokołu wymagają zachowania rezultatu `result.txt`, limitu czterech plików pamięci, liczników oraz źródeł skilla. W przypadkach eval zachowaj wejściowy kod i testy; pamięć koordynatora nie jest tworzona. Brak zmierzonego kosztu nie jest kosztem zerowym. Nie oczekuj identycznego sformułowania notatek; oceniaj decyzję i jej skutki.

Pełny test wykonania wymaga osobnego zadania z rzeczywistymi artefaktami oraz śladami powołań, modeli, napraw i niezależnego eval. Ten zestaw nie potwierdza faktycznej eskalacji Luna → Sol, jakości rzeczywistych porównań A/B ani statystycznej poprawy skuteczności. Kolejne wydania można porównywać na tych samych wejściach, ale mała liczba przejść nie daje wiarygodnej uniwersalnej oceny procentowej.

Raport pierwszego wydania: [v1.0.0](results-v1.0.0.md).

Raport weryfikacji rezultatu i zabezpieczeń: [v1.1.0](results-v1.1.0.md).

Porównanie organizacji pracy i przekazania wyniku: [v1.2.0](results-v1.2.0.md).
