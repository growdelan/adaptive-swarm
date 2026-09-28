# v1.2.1 — porównanie pełnego wykonania A/B

Data: 2026-09-28.

Przywrócono instrukcję sprzed rozszerzenia inspirowanego Team Topologies: usunięto 113 słów netto o granicach podzadań i przekazywaniu wyników. Osiem rzeczywistych implementacji nie wykazało przewagi dodatku w głównej mierze. Powrót do krótszej instrukcji jest decyzją o ograniczeniu tekstu bez potwierdzonego dodatkowego efektu, a nie deklaracją statystycznej poprawy jakości lub szybkości.

## Warianty i metoda

- **A:** `091b9d7b86a9767502c0268e26454faac1d5ee6e`, instrukcja z v1.1.0, 1134 słowa w SKILL.md.
- **B:** `1d29480feff9c6d3db80c53cb9851c680f14c172`, v1.2.0, 1247 słów.
- Wszystkie cztery pliki pakietu v1.2.1 odpowiadają dokładnie wariantowi A. Trzy pliki pomocnicze były identyczne w A i B.
- Dwa projekty Python/stdlib: przetwarzanie zamówień CSV z dokładnymi obliczeniami i raportami oraz walidacja grafu zadań z harmonogramem i zapasem czasu. Dwa powtórzenia każdego projektu i wariantu.
- Każdy przebieg: świeży koordynator `gpt-6-astra/high`, trzech rzeczywistych wykonawców `gpt-6-sol/medium` i osobny ewaluator `gpt-6-sol/medium`. Maksymalnie dwóch wykonawców naraz; trzeci i ewaluator byli kolejkowani.
- Specyfikacje, główne testy zewnętrzne, wzorce, kolejność i miary zamrożono przed próbami. Autor projektów nie znał wariantów skilla. Wzorce zaliczyły 19/19 i 17/17 przypadków; szkielety 0.
- Główna miara: wynik zewnętrznych testów CLI na pierwszym złożeniu wkładów, zachowanym przed poprawkami koordynatora. Druga ocena dotyczyła wyniku końcowego. Wcześniejsze kontrole wykonawców były dozwolone.
- Aktorzy nie otrzymywali testów zewnętrznych, wzorców, oznaczenia wariantu, hipotezy ani wcześniejszych wyników. Świeże konteksty i zakaz odczytu innych prób nie były systemową izolacją plików.
- Limit 12 minut i trzech prób celu na przebieg. Z góry przyjęto, że remis nie uprawnia do ogłoszenia skuteczności rozszerzenia.

## Wyniki główne

| Próba | Projekt | Wariant | Pierwsze złożenie | Wynik końcowy | Próby celu | Pliki produktu zmienione po złożeniu |
| --- | --- | --- | --- | --- | --- | --- |
| r01 | Zamówienia | A | 19/19 | 19/19 | 2 | 2 |
| r02 | Zamówienia | B | 19/19 | 19/19 | 2 | 2 |
| r03 | Harmonogram | B | 17/17 | 17/17 | 2 | 1 |
| r04 | Harmonogram | A | 17/17 | 17/17 | 1 | 0 |
| r05 | Zamówienia | B | 19/19 | 19/19 | 2 | 1 |
| r06 | Zamówienia | A | 19/19 | 19/19 | 2 | 3 |
| r07 | Harmonogram | A | 17/17 | 17/17 | 1 | 1 |
| r08 | Harmonogram | B | 17/17 | 17/17 | 1 | 1 |

Główna miara to remis 4/4 zaliczonych przebiegów na wariant, zarówno na początku, jak i na końcu. Próby celu sumują się do A: 6, B: 7; zmienione pliki produktu do A: 6, B: 5. Nie są to porównywalne miary kosztu: r06, r07 i r08 zawierają poprawki jeszcze przed pierwszym werdyktem. Nie mierzono tokenów ani kosztu finansowego; logi wiadomości nie są kompletnymi śladami komunikacji.

## Dodatkowe przypadki — analiza eksploracyjna

Po ujawnieniu usterek przez oceny i kontrole koordynatorów zebrano dodatkowe przypadki, a po zakończeniu ośmiu prób zastosowano je jednakowo do wszystkich pierwszych i końcowych wyników właściwego projektu:

- Zamówienia: błędny argument `--tax-rate -NaN`, poprawne pole `sku` długości 140 000 znaków i poprawna ilość zapisana jako 5000 zer zakończonych `1`.
- Harmonogram: niedozwolone stałe JSON `NaN`, `Infinity`, `-Infinity` pod dodatkowym kluczem. Trzy stałe sprawdzają jeden rodzaj usterki, nie trzy niezależne obserwacje.

| Komplet dodatkowych przypadków dla projektu | A | B |
| --- | --- | --- |
| Pierwsze złożenie | 1/4 przebiegów | 0/4 przebiegów |
| Wynik końcowy | 4/4 przebiegów | 2/4 przebiegów |

W końcowych r02 i r05 pozostał błąd odrzucania poprawnego CSV z długim `sku` jako `io_error`, wynikający z domyślnego limitu biblioteki. Specyfikacja nie ograniczała długości tego pola. A obsługiwał go poprawnie po naprawach. Dobór przypadków po odkryciu błędów oznacza, że nie jest to wcześniej ustalony test przewagi A ani dowód, że instrukcja B spowodowała regresję.

Naprawy dotyczyły głównie walidacji i granic bibliotek. W r02/B i r06/A importer dopuszczał ilość z wieloma zerami, której moduł obliczeń nie umiał przetworzyć. To niespójność na styku modułów obecna w obu wariantach, bez pewnej atrybucji do reguł koordynacji. Krótszy wariant także uzgadniał interfejsy i własność plików.

## Audyt pod Astrę i decyzja

Uwzględniono [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Artykuł uzasadnia ocenę nadmiernych instrukcji i warunkowe ładowanie dokumentacji, nie automatyczne usuwanie konkretnego protokołu. Niezależny audyt Astry, bez znajomości wyników prób, zalecił zachowanie konstrukcji skilla. Osobny recenzent Sol po zakończeniu badania, bez dostępu do sugerowanego wniosku, potwierdził remis głównej miary i eksploracyjny charakter różnic.

Zachowano ręczne wywołanie, dobór modeli, niezależną ocenę, cztery pliki pamięci, wznowienie, liczniki i zasady uczenia lokalnej strategii. Aktualizacja nie wymaga migracji pamięci. Nie wdrażano innych redakcyjnych propozycji z audytu: nie były wariantem tego porównania.

## Ograniczenia i odstępstwa

- Osiem przebiegów, dwie rodziny dobrze opisanych projektów ze szkieletem kodu: cztery porównania A/B. Przypadki wewnątrz projektu nie zwiększają liczby niezależnych powtórzeń. Nasycenie głównej miary ogranicza jej zdolność rozróżniania wariantów.
- Stała obsada trzech wykonawców i obowiązkowa kopia przed poprawkami zmieniają naturalny workflow, choć jednakowo dla A/B. Nie badano optymalnej liczebności, dużego roju, koordynatorów Sol/Luna, wznowienia po długiej przerwie ani całego skilla względem pracy bez niego.
- W r04 wykonawca dopisał test po zgłoszeniu gotowości i wykonaniu kopii. Kod produktu nie zmienił się, kopia pozostała nienaruszona; główne wyniki nie zależą od dopisanego testu.
- W r05 zaobserwowanie zakończenia nastąpiło po około 12 min 4 s od uruchomienia, a znacznik zakończenia aktora po około 11 min 36 s. Czas obserwacji nie jest dokładnym czasem wykonania.
- Sumy kontrolne potwierdziły zachowanie zamrożonych wejść, wariantów i pierwszych kopii. Nie dowodzą braku każdego możliwego odczytu innego katalogu; brak pełnej telemetrii narzędzi.
- Brak dowodu przewagi B nie jest dowodem braku efektu we wszystkich zastosowaniach. Wydanie nie deklaruje zmierzonej oszczędności ani statystycznej wyższości A.

## Dowody i odtworzenie

Załącznik [benchmark-evidence-v1.2.1.zip](https://github.com/growdelan/adaptive-swarm/releases/download/v1.2.1/benchmark-evidence-v1.2.1.zip) zawiera warianty, projekty, testy, pierwsze i końcowe wyniki, oceny oraz aparaturę. Historyczne ścieżki tymczasowe w logach odpowiadają katalogom wewnątrz archiwum. `study/reproduce.md` opisuje odtworzenie; `study/collect.py r01` ponownie ocenia wybrany przebieg, `study/supplementary.py` dodatkowe przypadki, a `study/verify_integrity.py` integralność. Potrzebny Python i biblioteka standardowa. Ponowne wykonanie pracy przez agentów może dać inne wyniki.
