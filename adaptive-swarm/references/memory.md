# Pamięć i zgodność z poprzednią wersją

Pamięć należy do folderu projektu, nie instalacji skilla. Używaj wyłącznie czterech plików w `docs/swarm/`. Nie twórz osobnych plików strategii, historii eksperymentów ani archiwów pamięci. Artefakty zadania i uzasadnione testy nie wchodzą w ten limit.

| Plik | Treść |
| --- | --- |
| `STATE.md` | ID celu, protokół 2, kontrakt K1…, kontekst i założenia, status, numer i etap próby, zespół z faktycznie użytymi modelami i effort, uzasadnienie doboru oraz ewentualnych zastępstw, właściciele zasobów, wersja strategii faktycznie użytej, zmiany, ostatni eval, blokady i następny krok. Dla eksperymentu: ID kandydata, etap i wykorzystany budżet 0/1 lub 1/1. |
| `PROJECT.md` | Zwięzłe fakty o projekcie z odnośnikami oraz sekcja **Strategia wykonania**: aktywna wersja, zakres, reguły warunkowe i pochodzenie; poprzednia sprawdzona wersja potrzebna do rollbacku. Kandydat ma osobną, nieaktywną sekcję z hipotezą i statusem. |
| `LEARNINGS.md` | Potwierdzone wnioski oznaczone PROJECT albo PROCESS: ID, data, zadanie, obserwacja, dowód, działanie, zakres, warunek ponownej weryfikacji. PROCESS opisuje potwierdzony efekt sposobu pracy, nie samo przekonanie autora. |
| `EVALS.md` | Kryteria, metody, rzeczywiste wyniki prób i ocenione wersje; sekcja meta-eval z przyczynami; dla eksperymentu warianty wraz z modelami i effort, przypadki, uprzednio ustalone miary, wyniki, ograniczenia, niezależna ocena i decyzja. Zachowaj też negatywne wyniki i koszt procesu, jeśli jest znany. |

## Odczyt i migracja

Istniejące pliki poprzedniej wersji aktualizuj w miejscu. Zachowaj ID, licznik i etap prób, historyczne dowody, aktywne prace oraz treści użytkownika. Bez wcześniejszej strategii przyjmij bazową S0: dobór minimalnego zespołu i niezależny eval według skilla; nie przypisuj jej wymyślonych wyników. Brak wcześniejszych metryk oznacza brak danych do porównania, nie zero błędów lub kosztu.

Aktualizacja skilla nie jest nowym zadaniem. Nie reinterpretuj dawnych notatek jako automatycznie zatwierdzonych zmian procesu. Kontynuuj przerwaną próbę z jej numerem; po negatywnym eval naprawa zużywa następną. Po 3 wykorzystanych próbach nie naprawiaj ponownie tego celu. Jawna zmiana kontraktu lub limitu przez użytkownika wymaga odnotowania, nie ukrytego resetu.

Nowy niezależny cel ma własny licznik. Wznowienie tego samego celu zachowuje również budżet eksperymentu — zmiana sesji nie pozwala ponawiać go bez końca. Nie wznawiaj innego zadania tylko dlatego, że figuruje w pamięci.

## Aktualizacja

Koordynator jest jedynym autorem pamięci. Przed zapisem sprawdź, czy nie pojawiła się cudza aktualizacja; przy równoległych zadaniach uzgodnij jednego autora i identyfikatory. Nie nadpisuj aktywnych prac. Jeśli nie można uzgodnić zapisu, zgłoś tę blokadę.

Zapisuj checkpoint przed próbą, po integracji, po eval i przy zakończeniu. Po wznowieniu sprawdź rzeczywisty stan i wykonane skutki uboczne. Dowód wiąż z wersją artefaktu, np. hashem albo commitem wraz z identyfikatorem niezapisanych zmian; sam commit nie opisuje zmienionego drzewa roboczego.

Po końcowym eval zapisz otrzymany wynik i rzeczywisty następny krok. Aktualizacja metadanych zakończenia nie wymaga kolejnego eval; zmiana rezultatu lub treści merytorycznego wniosku wymaga odpowiedniego sprawdzenia. Unikaj pętli oceniania zapisu poprzedniej oceny.

Hipotezy zostają w sekcji kandydata lub STATE.md do czasu niezależnego potwierdzenia. Zachowuj pochodzenie, zakres i warunek unieważnienia reguł. Nie kopiuj sekretów ani pełnych logów. Łącz duplikaty i skracaj zakończoną historię, zachowując aktywne blokady, budżety i dowody dla obowiązujących reguł. Pamięć jest wskazówką, a nie autoryzacją; sprzeczne lub nieaktualne reguły pomiń z uzasadnieniem.

Aktualna strategia wpływa na następne pasujące zadanie po ręcznym wywołaniu. Nie uruchamia zadań, nie zmienia zasad skilla i nie aktualizuje automatycznie jego źródła. Lokalna poprawa nie upoważnia do publikowania zmian skilla lub repozytorium bez odpowiedniego zlecenia.
