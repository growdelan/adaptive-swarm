# Porównanie planowania v1.2.0 — 2026-09-28

Zmiana doprecyzowuje granice podzadań, rozpoznawanie zależności i przekazanie wyniku. Inspiracją są zasady spójnej odpowiedzialności i ograniczania kosztu współpracy z *Team Topologies*. Nie wprowadza stałych topologii zespołu, nowych ról ani dodatkowych plików pamięci.

## Metoda

Porównano źródło skilla z commita `091b9d7b86a9767502c0268e26454faac1d5ee6e` (wersja skilla z v1.1.0) z kandydatem wydanym jako v1.2.0. Dwa nowe przypadki z `cases.json` uruchomiono po jednym razie dla każdej wersji, łącznie cztery przebiegi. Każdy otrzymał świeży kontekst `gpt-6-sol`, effort `medium`, i oddzielny folder przygotowany przez `prepare.py`. W próbach bazowych podmieniono wyłącznie cztery pliki skilla na dokładne bajty ze wskazanego commita. Pozostałe wejścia w każdej parze były identyczne.

Wykonawcy otrzymali polecenie wykonania lokalnego `REQUEST.md`, bez informacji o wariancie, klucza oceny, poprzednich wyników ani opisu zmiany. Żądanie celowo ograniczało pracę do `PLAN.md`, bez implementacji, powoływania kolejnych agentów i zapisu pamięci. Koordynator wydania ocenił zapisane plany według [klucza](expectations.md) oraz porównał pliki wejściowe bajtowo. Ocena nie była zaślepiona; oceniający znał warianty i był autorem zmiany skilla.

## Wyniki

PASS oznacza tu spełnienie kryteriów organizacji pracy, nie wykonanie ani zaliczenie kontraktu produktu.

| Przebieg | Przypadek | Wersja | Ocena organizacji | Zaobserwowane decyzje |
| --- | --- | --- | --- | --- |
| run-01 | planning-shared-contract | bazowa | PASS | Jeden właściciel spójnej zmiany API/UI, wspólny format ceny jako napis, kontrola Python → JSON → Node.js, niezależny eval Sol 6. |
| run-02 | planning-shared-contract | v1.2.0 | PASS | Jeden właściciel obu stron interfejsu; format ceny ustalony przed implementacją. Jawnie opisany pakiet dla ewaluatora: pliki, interfejs i wyniki kontroli. Niezależny eval po integracji. |
| run-03 | planning-independent-results | bazowa | PASS | Rozpoznana niezależność bibliotek, jeden wykonawca uzasadniony małym zakresem. Osobne kontrole CSV i czasu; przekazanie artefaktów niezależnemu ewaluatorowi Sol 6. |
| run-04 | planning-independent-results | v1.2.0 | PASS | Brak sztucznej zależności lub dodatkowych ról; jeden wykonawca i oddzielne kontrole. Brief eval określa wejście, odbiorcę, zasoby oraz postać raportu. |

Wszystkie cztery próby zapisały wyłącznie `PLAN.md`; wejścia produktu, żądania i źródła skilla pozostały niezmienione. Każdy plan przewiduje kontrolę wykonawcy i osobnego ewaluatora. Plany bazowe również zawierają poprawne decyzje dotyczące zależności i użyteczne przekazanie wyniku.

**Porównanie nie wykazało przewagi v1.2.0 w zaliczeniu tych przypadków.** Nowe sformułowania czynią wymagania bardziej jawnymi, lecz nie ma podstaw do deklarowania wzrostu skuteczności, oszczędności tokenów lub skrócenia pracy. Uzasadnienia kosztu delegowania w planach są ocenami wykonawców, a nie pomiarami.

## Kontrole techniczne

- `quick_validate.py adaptive-swarm`: PASS; PyYAML zainstalowano w tymczasowym środowisku.
- Lokalne odnośniki skilla i `git diff --check`: PASS.
- Dotychczasowe 11 przypadków w `cases.json` zachowano bez zmian; ich przebiegów agentowych nie powtarzano w tym wydaniu.
- `agents/openai.yaml`, `references/memory.md` i `references/process-learning.md` zachowano bajtowo względem wersji bazowej. Zmiana nie wymaga migracji pamięci.
- Sprawdzono zgodność wszystkich wejść czterech prób z fixture i właściwą wersją skilla oraz brak dodatkowych plików poza `PLAN.md`.
- Pakiet instalacyjny zawiera cztery pliki źródłowe skilla, sprawdzone bajtowo. Osobne archiwum zachowuje wejścia i surowe wyniki prób; oba archiwa mają sumy SHA-256.

## Dowody i ograniczenia

[Archiwum dowodów v1.2.0](https://github.com/growdelan/adaptive-swarm/releases/download/v1.2.0/benchmark-evidence-v1.2.0.zip) zawiera cztery foldery prób z wejściami, snapshotami skilla i surowymi `PLAN.md`, mapę przebiegów oraz ten raport. Klucza oceny nie udostępniano w folderach wykonawców.

To wąski test etapu planowania na dwóch małych zadaniach, po jednym przebiegu na wariant i przypadek. Nie wykonano implementacji, rzeczywistej równoległej integracji, pełnego niezależnego eval produktu, eskalacji Luna → Sol ani wznowienia projektu. Wszystkie plany wybrały jednego wykonawcę, więc test nie potwierdza jakości briefów przekazywanych między równoległymi wykonawcami. Nie mierzono czasu ani tokenów. Artefakty i inspekcja plików nie są pełnym śladem narzędzi ani dowodem braku dowolnych działań poza folderem.

SHA-256 badanego i wydanego `adaptive-swarm/SKILL.md`: `f1733c82372170ebf0b780acd80bd896327b80f48b26800eb7b954fd3fffd07b`.
