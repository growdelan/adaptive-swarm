# Weryfikacja v1.0.0 — 2026-09-26

Zakres źródła: folder `adaptive-swarm/` w tagu `v1.0.0`. Scenariusze: `cases.json` z tego samego tagu. Model wykonujący każdy przypadek: `gpt-6-sol`, effort `medium`, świeży kontekst, oddzielny folder. Oceniający: koordynator wydania, który przygotował wejścia, ale nie tworzył wynikowych zapisów agentów. Wykonawcy nie otrzymali klucza odpowiedzi. Historia porównań E1/E2 jest syntetyczna, nie została rzeczywiście wykonana.

| Przypadek | Wynik decyzji | Dowód z faktycznie zapisanych artefaktów |
| --- | --- | --- |
| first-confirmation | PASS | PROJECT: „C1, PENDING”, „1 z 2”; aktywna S0. EVALS wylicza koszt +1 i wskazuje brak drugiego potwierdzenia. STATE zachowuje G1 DONE, próbę 1/3 i eksperyment 1/1. |
| second-confirmation | PASS | PROJECT zawiera S1, poprzednią S0 i regułę S1-R1 opartą na E1/E2. EVALS porównuje koszt +1/+2 z limitem 2 i potwierdza drugi przypadek; STATE zachowuje strategię faktycznie używaną w G2 jako S0 oraz liczniki. |
| rule-conflicts | PASS | STATE: R2 przed R1, R3 pominięta, planowany ewaluator gpt-6-sol/medium, R4/R5 pominięte z lokalnym S0, R6 z wyjątkiem R7. PROJECT zachowuje S4. Niezależny wynik zapisanej decyzji był prawidłowo pozostawiony prowadzącemu test. |
| done-inefficiency | PASS | EVALS rozpoznaje dwa odczyty przy jednej potrzebie; PROJECT zapisuje jednego kandydata C1 PENDING, 0 potwierdzeń, z miarą liczby odczytów. STATE zachowuje DONE, próbę 1/3 i eksperyment 0/1. Brak deklaracji oszczędności czasu/tokenów. |
| attempts-exhausted | NOT RUN | Przypadek przygotowany do kolejnych regresji; brak wykonania w tym wydaniu. |
| missing-evidence | NOT RUN | Przypadek przygotowany do kolejnych regresji; brak wykonania w tym wydaniu. |
| over-budget | NOT RUN | Przypadek przygotowany do kolejnych regresji; brak wykonania w tym wydaniu. |
| rollback | NOT RUN | Przypadek przygotowany do kolejnych regresji; brak wykonania w tym wydaniu. |

Wykonano cztery powyższe testy decyzji: 4 PASS. Inspekcja wszystkich czterech kompletów pamięci potwierdziła decyzje i liczniki. Dodatkowo porównano bajtowo `result.txt` oraz każdy plik skilla z wejściem, a listę plików `docs/swarm/` z wymaganymi czterema nazwami: bez odstępstw.

## Kontrole techniczne

- `quick_validate.py adaptive-swarm`: PASS.
- `git diff --check`: PASS.
- Helper przygotował wszystkie osiem przypadków: treść żądań i fixture zgodna z JSON, kopie skilla zgodne bajtowo, brak klucza odpowiedzi. Ponowne użycie istniejącego folderu oraz folder docelowy wewnątrz repozytorium zostały odrzucone.
- Niezależny read-only review przez `gpt-6-sol/high`: brak istotnych usterek i sprzeczności instrukcji.
- Archiwum wydania zawiera dokładnie cztery pliki skilla, zgodne bajtowo ze źródłem; dołączono SHA256SUMS.

## Ograniczenia

PASS oznacza poprawną decyzję w danym teście oraz sprawdzone artefakty. Nie oznacza wykonania historycznych eksperymentów A/B, dowodu oszczędności ani pełnego testu od celu do produktu. Testy nie powoływały zespołów wewnętrznych; nie sprawdzono rzeczywistej eskalacji Luna → Sol. Zewnętrzny odczyt plików i porównanie bajtów nie dowodzą braku wszystkich możliwych działań poza folderem. Surowe foldery testowe były tymczasowe; wejścia i procedura odtworzenia pozostają w repozytorium, a powyższe dowody są skrótem inspekcji wyników.

## Identyfikacja przetestowanego pakietu

SHA-256 plików źródłowych (przed pakowaniem):

```text
bd94b2f5ba21066f7dba6a4714bc785bde8ec2af2955b80172e12d624ad77bed  adaptive-swarm/SKILL.md
2a0c851cda4b31837ea96ac43e2d1b56996f4852e55a66a8d3ed1faff9652bbc  adaptive-swarm/agents/openai.yaml
4fbed0fd6fdf41bba534a4efa11d3d9bca3609adcd8ccaace1e60f0bb697dbfe  adaptive-swarm/references/memory.md
d99b45ed55bedff4062438f7fa197e8c907a41ee21224abb7a78cb3337b779ed  adaptive-swarm/references/process-learning.md
```
