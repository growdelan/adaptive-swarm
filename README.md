# Adaptive Swarm

Skill do ręcznej realizacji zadań w Codex przez zespół dobierany do faktycznej trudności pracy. Łączy wykonanie, niezależną ocenę wyniku oraz doskonalenie lokalnej strategii projektu na podstawie dowodów.

Koordynatorem pozostaje model wybrany w rozmowie. Powoływani agenci korzystają z `gpt-6-sol` lub `gpt-6-luna`: Luna wykonuje najlżejsze, jednoznaczne podzadania, a Sol obsługuje trudniejsze prace i zawsze odpowiada za niezależny eval oraz meta-eval. Skill dobiera najmniejszy skuteczny zespół.

## Zawartość repozytorium

```text
adaptive-swarm/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── memory.md
    └── process-learning.md
benchmarks/                 # scenariusze i raporty, poza pakietem skilla
README.md
```

- [SKILL.md](adaptive-swarm/SKILL.md) — zasady uruchomienia, dobór zespołu i pętla dostarczenia.
- [memory.md](adaptive-swarm/references/memory.md) — zapis stanu i wznowienie pracy.
- [process-learning.md](adaptive-swarm/references/process-learning.md) — porównywanie i zatwierdzanie zmian strategii.

## Instalacja w projekcie

Potrzebujesz Codex z narzędziami powoływania agentów i dostępem do wymaganych modeli. Samo skopiowanie plików nie udostępnia modeli ani narzędzi. Przy braku Luny skill dopuszcza zastępstwo Solem; brak Sola do wymaganej roli albo niezależnej oceny musi zostać zgłoszony jako ograniczenie.

Sklonuj to repozytorium do osobnego katalogu:

```bash
git clone https://github.com/growdelan/adaptive-swarm.git
```

W katalogu projektu, w którym chcesz pracować, skopiuj **wewnętrzny folder skilla**. Zastąp `/sciezka/do/adaptive-swarm` ścieżką do sklonowanego repozytorium:

```bash
mkdir -p .agents/skills
cp -R /sciezka/do/adaptive-swarm/adaptive-swarm .agents/skills/
```

Docelowy plik powinien znaleźć się pod ścieżką:

```text
twoj-projekt/.agents/skills/adaptive-swarm/SKILL.md
```

Powyższe polecenie zakłada pierwszą instalację. Przy aktualizacji zastąp istniejący folder skilla świadomie, zachowując własne modyfikacje i pamięć projektu w `docs/swarm/`.

Otwórz właściwy projekt w Codex. Skill powinien zostać wykryty automatycznie; jeśli nie pojawi się na liście, uruchom Codex ponownie. Lokalizacje instalacji i sposób wywoływania opisuje [oficjalna dokumentacja OpenAI](https://learn.chatgpt.com/docs/build-skills).

Opcjonalnie dodaj `.agents/skills/adaptive-swarm/` do Git projektu, aby zespół korzystał z tej samej wersji. Folder `adaptive-swarm/` w tym repozytorium jest pakietem źródłowym — samo sklonowanie repozytorium nie umieszcza go w lokalizacji wykrywania skilli projektu.

## Jak rozpocząć zadanie

Wywołaj skill jawnie przez `$adaptive-swarm`, wybór w interfejsie albo jednoznaczne polecenie użycia go po nazwie. Automatyczne dopasowanie jest wyłączone w `agents/openai.yaml`. Nie trzeba dopisywać protokołu do `AGENTS.md` ani tworzyć automatycznych wyzwalaczy.

Podaj wynik, kontekst i sprawdzalne warunki ukończenia, np.:

```text
$adaptive-swarm
Cel: Dodaj eksport listy zamówień do CSV w tym projekcie.
Kontekst: Pracuj w bieżącym repozytorium. Zachowaj istniejące uprawnienia
użytkowników i format dat. Nie wdrażaj aplikacji.
Kryteria:
K1: Użytkownik może pobrać zamówienia widoczne po zastosowaniu filtrów.
K2: CSV zawiera nagłówki i poprawnie obsługuje przecinki oraz polskie znaki.
K3: Istniejące testy dla zmienionego modułu przechodzą.
```

Koordynator ustala kontrakt, punkt odniesienia, zespół i sposób weryfikacji. Następnie wykonuje oraz integruje pracę, a niezależny ewaluator sprawdza każde kryterium jako `PASS`, `FAIL` albo `UNVERIFIED`.

Na jeden cel przypadają maksymalnie **trzy próby**: pierwsze rozwiązanie i dwie rundy napraw po negatywnym eval. Zwykłe kroki wykonania i kontrole wstępne mieszczą się w bieżącej próbie. Wynik `DONE` wymaga `PASS` wszystkich obowiązkowych kryteriów dla zintegrowanego rezultatu oraz zapisanej pamięci.

## Gdzie zapisywana jest pamięć

Pamięć powstaje w **projekcie, nad którym pracujesz**, a nie w folderze instalacji skilla:

| Plik | Do czego służy |
| --- | --- |
| `docs/swarm/STATE.md` | ID i kontrakt celu, status, numer i etap próby, zespół, użyta strategia, blokady i następny krok. |
| `docs/swarm/PROJECT.md` | Fakty o projekcie, aktywna strategia wykonania, poprzednia wersja do rollbacku i ewentualny kandydat zmiany. |
| `docs/swarm/LEARNINGS.md` | Potwierdzone wnioski o projekcie i procesie wraz z dowodami oraz zakresem zastosowania. |
| `docs/swarm/EVALS.md` | Wyniki ocen, metody sprawdzenia, meta-eval i ewentualne porównanie strategii. |

Te cztery pliki zapisuje koordynator. Checkpointy powstają przed próbą, po integracji, po eval i przy zakończeniu. Nie musisz tworzyć pustych plików przed pierwszym uruchomieniem.

## Jak kontynuować rozpoczętą pracę

### W tej samej rozmowie

Wskaż, że chodzi o ten sam cel i zachowujesz jego kontrakt:

```text
Kontynuuj rozpoczęty cel adaptive-swarm zgodnie z docs/swarm/STATE.md.
Zachowaj kryteria, numer próby i dotychczasowe ustalenia.
```

Jeśli prosisz o przerwanie pracy, poproś również o checkpoint:

```text
Zapisz aktualny stan adaptive-swarm w docs/swarm/, w tym numer i etap
próby, wykonane zmiany, dowody, blokady oraz następny krok. Następnie
wstrzymaj pracę nad tym celem.
```

### W nowej rozmowie lub po ponownym otwarciu projektu

Otwórz ten sam projekt i jawnie uruchom skill ponownie. Przykład:

```text
$adaptive-swarm
Wznów ten sam, niezakończony cel zapisany w docs/swarm/STATE.md.
Przeczytaj kontrakt pamięci oraz aktywną strategię w docs/swarm/PROJECT.md.
Sprawdź rzeczywisty stan plików, gałąź, niezapisane zmiany i wykonane
działania. Zachowaj ID celu, kryteria, numer i etap próby oraz wykorzystany
budżet eksperymentu. Kontynuuj od zapisanego następnego kroku w ramach
dotychczasowego zakresu.
```

Jeżeli w projekcie jest kilka celów, podaj ID tego, który chcesz wznowić. Gdy zmieniły się wymagania lub została usunięta blokada, dopisz konkretną zmianę. Samo otwarcie projektu ani obecność pamięci nie uruchamia skilla.

Wznowienie odtwarza kontrakt i stan z plików, ale nie przywraca automatycznie żywych agentów ani całej historii poprzedniego czatu. Dlatego koordynator musi sprawdzić aktualny kod i skutki już wykonanych działań, zanim je powtórzy. Po awaryjnym zamknięciu stan na dysku może być nowszy niż ostatni checkpoint.

**Zmiana rozmowy, modelu lub wersji skilla nie zeruje licznika.** Przerwana próba zachowuje numer; naprawa po negatywnym eval zużywa następną. Po trzech wykorzystanych próbach skill zatrzymuje naprawy tego celu. Jawna zmiana kontraktu lub limitu przez użytkownika musi zostać odnotowana.

### Kontynuowanie na innym komputerze lub checkoutcie

Przenieś zarówno wynik pracy, jak i cztery pliki `docs/swarm/`. Jeśli używasz Git, zapisz odpowiednie zmiany w commicie i pobierz właściwą gałąź na drugim komputerze. Uwzględnij potrzebne pliki nieśledzone — sam commit nie przenosi niezapisanych zmian. Upewnij się, że w docelowym projekcie jest także zainstalowany skill.

Pamięć nie powinna zawierać sekretów ani pełnych logów. Nie publikuj jej automatycznie razem z tym repozytorium skilla; należy do konkretnego projektu.

## Kolejne zadanie i uczenie strategii

Po ukończeniu celu uruchom `$adaptive-swarm` z **nowym Celem, Kontekstem i Kryteriami**. Nowy niezależny cel otrzymuje własny licznik prób, a potwierdzone wnioski oraz pasująca aktywna strategia projektu mogą zostać wykorzystane ponownie. Skill nie wybiera sam kolejnego zadania z roadmapy.

Przy powtarzającym się problemie procesu lub udokumentowanej nieefektywności mimo `DONE` może zaproponować jedną zmianę strategii i wykonać najwyżej jeden ograniczony eksperyment porównawczy na wywołanie. Wznowienie tego samego celu zachowuje wykorzystany budżet eksperymentu. Bez wystarczających dowodów kandydat pozostaje `PENDING`; poprawnie ukończone zadanie nie wymaga udanego eksperymentu.

Mała zmiana wymaga jednego potwierdzenia. Zmiana o dużym wpływie — np. dodatkowy agent przy szerokiej klasie zadań — wymaga dwóch potwierdzeń na różnych pasujących przypadkach; drugie zbiera się w kolejnym ręcznie zleconym zadaniu. Samo `DONE` nie dowodzi korzyści procesu.

Przy konflikcie strategii obowiązuje bieżący kontrakt i ograniczenia skilla. Wśród zgodnych, potwierdzonych reguł pierwszeństwo mają jawny wyjątek i bardziej szczegółowy zakres, a nie sama nowsza data. Nierozstrzygnięty konflikt oznacza pominięcie konfliktujących reguł, powrót w tym zakresie do zasad bazowych i zapis uzasadnienia.

Zweryfikowana zmiana trafia do lokalnej strategii w `PROJECT.md`. Skill nie przepisuje automatycznie własnego źródła ani globalnej konfiguracji.

## Jak czytać raport końcowy

- `DONE` — wszystkie obowiązkowe kryteria mają `PASS`, a pamięć została zapisana.
- `NOT_COMPLETED` — cel nie został ukończony, np. wyczerpano limit prób.
- `BLOCKED` — istnieje rzeczywista przeszkoda uniemożliwiająca dalszą pracę.

Raport zawiera rezultat i odnośniki, wykorzystane próby, dowody dla kryteriów, wersję strategii, wynik meta-eval oraz decyzję: bez zmiany / `PENDING` / `ACTIVE` / `REJECTED` / `ROLLED_BACK`. `UNVERIFIED` oznacza brak potwierdzenia, a nie zaliczenie kryterium.

Szczegółowy kontrakt pozostaje w plikach skilla.

## Testowanie i wydania

[Scenariusze regresyjne](benchmarks/README.md) pozwalają przygotować izolowane przypadki, odtworzyć decyzje protokołu i ocenić rzeczywiste artefakty oraz działania. Nie są ładowane podczas zwykłego używania skilla. Wyniki rozróżniają test decyzji od pełnego wykonania zadania; nie stanowią procentowej oceny skuteczności na dowolnych projektach.

Wersje pakietu są oznaczane tagami. [GitHub Releases](https://github.com/growdelan/adaptive-swarm/releases) zawiera opis zmian i archiwum instalacyjne. Nazwa wywołania pozostaje `$adaptive-swarm`, niezależnie od numeru wydania.
