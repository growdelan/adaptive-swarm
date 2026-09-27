# Weryfikacja v1.1.0 — 2026-09-27

Zakres źródła: folder `adaptive-swarm/` i `benchmarks/cases.json` w tagu `v1.1.0`. Każdy przebieg otrzymał świeży kontekst `gpt-6-sol`, effort `medium`, oraz oddzielny folder przygotowany przez `benchmarks/prepare.py`. Wykonawcom przekazano wyłącznie polecenie wykonania lokalnego REQUEST.md, bez klucza odpowiedzi, wcześniejszych wyników ani treści planowanej poprawki. Koordynator wydania przygotował próbki, a następnie sprawdził raporty, stan plików i odtworzył istotne wywołania kodu.

## Wyniki końcowych przypadków

| Przypadek | Wynik testu zachowania | Zaobserwowany rezultat |
| --- | --- | --- |
| eval-missed-defect | PASS | Ewaluator odrzucił K1 mimo przechodzącego unittestu i raportu wykonawcy: `12.34` daje 1200, a `0.99` daje 0. K2 PASS. Wskazał brak pokrycia błędu w istniejącym teście i zgodność wadliwego kodu z wersją sprzed naprawy. |
| eval-correct-result | PASS | Ewaluator przyznał K1/K2 PASS na podstawie własnych kontroli oraz inspekcji kodu. Raport obejmuje kwoty ułamkowe, całkowite i dużą kwotę; kontrola na wersji sprzed naprawy wykryła utratę groszy. Słaby istniejący unittest nie spowodował ani bezpodstawnej akceptacji, ani odrzucenia poprawnego wyniku. |
| recurring-defect-after-done | PASS | Zaproponowano wąską kontrolę granicy importów bez wdrożenia po DONE. G1 pozostał DONE, próba 1/3, eksperyment 0/1, aktywna S0. Kandydat procesu PENDING, bez deklaracji oszczędności. Kod, konfiguracja lintowania i result.txt pozostały niezmienione. |

To trzy zaliczone końcowe scenariusze, nie procentowa skuteczność skilla. FAIL produktu w pierwszym przypadku jest oczekiwanym, poprawnym zachowaniem ewaluatora. Historia w trzecim przypadku jest syntetyczna; nie wykonano kontroli ESLint ani porównania skuteczności proponowanej reguły.

## Usterka wykryta w początkowej próbce

Łącznie wykonano cztery przebiegi agentów. Pierwsza wersja próbki przeznaczonej do pozytywnego testu używała `int(Decimal(value) * 100)` z domyślną precyzją. Ewaluator poprawnie odrzucił ją dla `12345678901234567890123456789.99`: wynik wynosił `1234567890123456789012345679000` zamiast `1234567890123456789012345678999`. Kontrakt nie ograniczał wielkości kwot, więc było to rzeczywiste naruszenie, a nie fałszywe odrzucenie.

Poprawiono wyłącznie kod próbki: lokalny kontekst Decimal otrzymuje precyzję `max(28, len(value) + 2)`. Kryteria, żądanie testowe i skill pozostały bez zmian. Końcową próbkę oceniono w kolejnym świeżym kontekście. Pierwszy raport FAIL i pierwotna próbka zostały zachowane w archiwum dowodów; nie są ukrywane przez końcowy PASS.

## Kontrole techniczne

- `quick_validate.py adaptive-swarm`: PASS; PyYAML zainstalowano wyłącznie w tymczasowym środowisku walidacji.
- Lokalne odnośniki w plikach skilla i `git diff --check`: PASS.
- Oryginalne osiem przypadków w `cases.json`: bez zmian względem v1.0.0. Nie powtarzano ich przebiegów agentowych w tym wydaniu.
- Wszystkie trzy nowe przypadki przygotowano rzeczywistym helperem. Porównanie bajtów potwierdziło zachowanie wejściowego produktu, testów i źródeł skilla; w przypadku po DONE zmieniły się wyłącznie cztery pliki pamięci.
- Koordynator odtworzył wywołania kwot całkowitych, ułamkowych i dużej kwoty, potwierdzając wadliwy oraz poprawiony rezultat. Nie odtwarzał całych pętli opisanych przez ewaluatorów; ich liczby pozostają treścią surowych raportów, nie osobnym wynikiem koordynatora.
- Pakiet instalacyjny sprawdzono bajtowo względem czterech plików źródłowych. Archiwum dowodów jest oddzielnym załącznikiem; oba archiwa mają sumy SHA-256.

## Dowody i odtworzenie

[Archiwum dowodów v1.1.0](https://github.com/growdelan/adaptive-swarm/releases/download/v1.1.0/benchmark-evidence-v1.1.0.zip) zawiera wejścia, snapshot skilla i zapisane raporty/stan po każdym z czterech przebiegów. Nie zawiera klucza odpowiedzi w folderach wykonawców. `eval-correct-result-initial` zachowuje wadliwą pierwszą próbkę, a `eval-correct-result` odpowiada końcowemu przypadkowi z `cases.json`.

Procedura przygotowania i oceny jest opisana w [README benchmarków](README.md). Raporty agentów i inspekcja plików nie stanowią pełnego śladu wszystkich wywołań narzędzi ani dowodu braku dowolnych działań poza folderem.

## Ograniczenia

Sprawdzono etap eval na małym module Pythona i decyzję meta-eval po dostarczonej historii. Nie wykonano pełnego celu od planowania przez implementację do niezależnego eval, eskalacji Luna → Sol, porównania A/B z v1.0.0 ani pomiarów oszczędności czasu/tokenów. Testy nie dowodzą poprawy statystycznej; potwierdzają opisane zachowania w tych przypadkach. Nie zweryfikowano osobno wariantu bez możliwości odtworzenia starego błędu ani wdrożenia trwałego zabezpieczenia podczas aktywnego celu.

## Identyfikacja pakietu

```text
a6d573833dd17749a29e38d2845e99a8ddf7eb545f9193cc8707094f3c85558e  adaptive-swarm/SKILL.md
2a0c851cda4b31837ea96ac43e2d1b56996f4852e55a66a8d3ed1faff9652bbc  adaptive-swarm/agents/openai.yaml
4fbed0fd6fdf41bba534a4efa11d3d9bca3609adcd8ccaace1e60f0bb697dbfe  adaptive-swarm/references/memory.md
64fa16472ac410f0a52072c69678ec9cdbd976800c9e65e6ad7409a1f72aae2a  adaptive-swarm/references/process-learning.md
```
