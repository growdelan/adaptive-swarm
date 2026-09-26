# Scenariusze regresyjne

Te przypadki sprawdzają decyzje protokołu przy zadanej historii. Są oddzielone od pakietu instalowanego skilla. Dane historyczne, oceny i pomiary w `cases.json` są syntetycznymi wejściami testu: nie stanowią dowodów, że rój osiągnął opisane korzyści w rzeczywistym projekcie.

## Odtworzenie

1. Z katalogu repozytorium wyświetl przypadki: `python3 benchmarks/prepare.py`.
2. Przygotuj przypadek w nowym folderze poza repozytorium, np. `python3 benchmarks/prepare.py first-confirmation /tmp/swarm-first-check`. Skrypt odmawia nadpisania istniejącego folderu. Kopiuje dokładny snapshot skilla, żądanie i dane wejściowe; nie kopiuje klucza odpowiedzi ani raportów.
3. Uruchom świeżą sesję Codex lub niezależnego subagenta z dostępem do tego folderu. Zleć: „Wykonaj REQUEST.md w tym folderze; pracuj tylko tutaj”. Do porównania wydań zachowuj model i effort; pierwsze testy używały `gpt-6-sol`, `medium`. Nie przekazuj wykonawcy oczekiwanego wyniku.
4. Po zakończeniu niezależnie sprawdź zmiany w plikach, nie tylko raport końcowy. [Klucz oceny](expectations.md) jest przeznaczony dla oceniającego. Zapisz wersję źródła, przypadek, model/effort, zaobserwowane działania, dowody i wynik PASS / FAIL / UNVERIFIED. Zmiana plików to dowód zapisu decyzji; deklaracja uruchomienia narzędzia nie dowodzi jego użycia.
5. Zachowaj raport i potrzebne artefakty przed usunięciem izolowanego folderu. Testy nie powinny publikować zmian ani korzystać z systemów produkcyjnych.

## Zakres i granice

To testy poszczególnych decyzji po dostarczonych ocenach, a nie pełne wykonanie od celu do niezależnego eval. Wyłączenie powoływania agentów w żądaniu testowym izoluje etap koordynacji i nie zmienia reguł zwykłego używania skilla. Ocena testowa jest wykonywana z zewnątrz.

Wszystkie przypadki wymagają zachowania rezultatu `result.txt`, limitu czterech plików pamięci, liczników oraz źródeł skilla. Brak zmierzonego kosztu nie jest kosztem zerowym. Nie oczekuj identycznego sformułowania notatek; oceniaj decyzję i jej skutki.

Pełny test wykonania wymaga osobnego zadania z rzeczywistymi artefaktami oraz śladami powołań, modeli, napraw i niezależnego eval. Ten zestaw nie potwierdza faktycznej eskalacji Luna → Sol, jakości rzeczywistych porównań A/B ani statystycznej poprawy skuteczności. Kolejne wydania można porównywać na tych samych wejściach, ale mała liczba przejść nie daje wiarygodnej uniwersalnej oceny procentowej.

Raport pierwszego wydania: [v1.0.0](results-v1.0.0.md).
