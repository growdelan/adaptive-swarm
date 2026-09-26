---
name: adaptive-swarm
description: Ręczna realizacja zadania przez adaptacyjny zespół Sol 6 i Luna 6, z niezależnym evalem i doskonaleniem strategii projektu na podstawie wyników.
---

# Adaptive Swarm

Dostarcz wynik określony przez **Cel, Kontekst i Kryteria**. Dobierz zespół do zadania, oceń rezultat niezależnie i wykorzystaj dowody do poprawiania sposobu pracy w tym projekcie. Zmiana procesu musi mieć mierzalne uzasadnienie; przyrost notatek nie dowodzi poprawy.

## Ręczny start

Uruchamiaj tylko przez `$adaptive-swarm`, wybór tego skilla w interfejsie lub jednoznaczne polecenie użycia go po nazwie. Wzmianka w materiale, plik pamięci ani pasujące zadanie nie są wywołaniem. Nie instaluj automatycznych wyzwalaczy i nie dopisuj tego protokołu do `AGENTS.md`.

```text
$adaptive-swarm
Cel: ...
Kontekst: ...
Kryteria: ...
```

Ustal folder i obowiązujące instrukcje. Przeczytaj istniejący `docs/swarm/STATE.md` oraz sekcję aktywnej strategii w `PROJECT.md`; pozostałą pamięć czytaj stosownie do zadania. Sprawdź aktualność zastosowanych faktów. Przy pierwszym zapisie, wznowieniu lub konflikcie reguł przeczytaj [kontrakt pamięci](references/memory.md). Skill korzysta z tych samych czterech plików co poprzednia wersja, bez resetowania rozpoczętych zadań.

Niepełne dane uzupełniaj jawnymi założeniami; pytaj tylko o niezbędne rozstrzygnięcia, których nie można ustalić. Niewypełniony szablon nie jest zadaniem. Rutynowe decyzje i kontynuacja w uzgodnionym zakresie nie wymagają ponownej zgody.

## Kontrakt i organizacja

Nadaj kryteriom identyfikatory K1… oraz przypisz dowody i warunki zaliczenia. Oddziel wymagania obowiązkowe od ulepszeń. Zapisz punkt odniesienia i wersję użytej strategii. Podzadania i kolejność dobieraj autonomicznie w obrębie tego celu; ukończenie celu nie upoważnia do wyboru następnego zadania z roadmapy.

Jeżeli użytkownik jawnie zlecił pracę na celu i narzędzie celu jest dostępne, użyj go zgodnie z jego zasadami. Nie zastępuj innego aktywnego celu. Kontrakt w STATE.md pozostaje źródłem przekazania również bez tego narzędzia.

Zaprojektuj najmniejszy skuteczny zespół. Koordynator może wykonać małe zadanie sam i powołać osobnego ewaluatora. Dodatkowe role uzasadniaj niezależną analizą, oszczędnością kontekstu lub równoległością. Nie powołuj dodatkowego agenta wyłącznie po to, aby wykorzystać Lunę 6. Aktywna strategia może zmienić podział pracy, kolejność, briefy, dobór modelu, effort i metody sprawdzania w granicach poniższych zasad.

- Do powoływanych agentów dobieraj wyłącznie `gpt-6-sol` lub `gpt-6-luna`. Koordynatorem jest model wybrany w rozmowie; skill nie przełącza go sam.
- Wybieraj `gpt-6-luna` do najlżejszych podzadań: wąskich, jednoznacznych, o niskich skutkach pomyłki i łatwym do sprawdzenia wyniku. Przykłady: wyszukanie wskazanych symboli, inwentaryzacja plików, ekstrakcja określonych pól, mechaniczna zmiana według ustalonego wzorca lub uruchomienie znanej kontroli. Oceń faktyczną trudność; mała liczba plików nie oznacza prostego zadania.
- W pozostałych przypadkach wybieraj `gpt-6-sol`: niejasne wymagania, architektura, diagnoza przyczyn, złożona implementacja, integracja wymagająca decyzji i istotne skutki błędu. Niezależny ewaluator wyniku, meta-ewaluator i agent zatwierdzający zmianę strategii zawsze używają Sol 6. Luna 6 może zebrać dane lub uruchomić kontrolę, ale nie zastępuje ich oceny.
- Jeśli podzadanie Luny 6 ujawnia niejednoznaczność, większy zakres lub niewiarygodny wynik, przekaż je do Sol 6 z ustaleniami i dowodami. Gdy Luna 6 jest niedostępna, użyj Sol 6 i odnotuj zastępstwo; gdy brakuje Sola do roli, która go wymaga, zgłoś ograniczenie. Zmiana modelu nie resetuje prób: naprawa po negatywnym eval zużywa kolejną próbę całego celu.
- Effort dobieraj niezależnie od modelu, spośród poziomów przez niego obsługiwanych. Punktem wyjścia jest `medium` dla Sol 6 i `high` dla Luny 6; dla jednoznacznych operacji można go obniżyć, a dla trudnej analizy podnieść z uzasadnieniem. Ustaw model i effort parametrami narzędzia. Gdy pełny fork wyklucza te parametry, użyj świeżego kontekstu i samowystarczalnego briefu.
- Tylko koordynator powołuje agentów i zapisuje pamięć. Kolejkuj pracę według dostępnych slotów. Każdy brief określa wynik, kryteria, kontekst, właściciela zasobów, zależności i wymagane dowody. Nie deleguj równoczesnych edycji tych samych zasobów.
- Ewaluator nie tworzy ani nie naprawia ocenianego wyniku. Może pełnić też rolę meta-ewaluatora, jeśli nie był autorem ocenianej zmiany procesu. Gdy nim był, ocenę porównania powierz innemu niezależnemu agentowi; nie trzeba utrzymywać osobnego stałego zespołu.
- Braku wymaganych narzędzi, modelu lub niezależnej oceny nie zastępuj deklaracją sukcesu ani symulowaniem agentów w tej samej rozmowie.

Krótko przedstaw skład, modele, effort i powody doboru, po czym wykonuj zadanie. Chronione są: ręczne wywołanie, zakres i zgody użytkownika, powyższe granice doboru modeli, niezależność eval, obowiązkowe kryteria, limit prób i limit plików pamięci. Strategia nie może ich zmieniać. Nie modyfikuj automatycznie źródła skilla ani globalnej konfiguracji; doskonal lokalną strategię wykonania.

## Pętla dostarczenia

**Maksymalnie trzy próby na cały cel:** pierwsze rozwiązanie i dwie rundy napraw po negatywnym eval. Podzadania, eksperyment, nowy agent, nowa sesja ani aktualizacja skilla nie otrzymują osobnego budżetu napraw tego samego celu.

Przed próbą zapisz numer i etap. Wykonaj, zintegruj i poddaj wynik niezależnemu eval. Ewaluator otrzymuje oryginalny kontrakt, sam sprawdza artefakty i dowody, a dla każdego K podaje PASS, FAIL lub UNVERIFIED. Sprawdzenie dobierz do zadania: test, obliczenie, źródła, inspekcja lub scenariusz użytkownika. Raport wykonawcy nie jest dowodem. Brak możliwości sprawdzenia nie jest PASS.

Po FAIL wskaż przyczynę, dowód i zmianę podejścia. Naprawa po negatywnym eval rozpoczyna następną próbę; zwykłe kroki wykonania i kontrole wstępne mieszczą się w próbie. Ponów sprawdzenia dotknięte zmianą i istotne regresje. Nie obniżaj kryteriów ani nie dodawaj nieskończonych „drobnych poprawek”. Po próbie 3 zatrzymaj naprawy; wcześniej zakończ przy rzeczywistej blokadzie.

## Pętla doskonalenia procesu

Przy zamknięciu zadania ewaluator krótko rozróżnia błąd rezultatu, problem środowiska i problem procesu. Brak istotnego sygnału oznacza „bez zmiany strategii”, bez dodatkowego agenta lub eksperymentu. Sukces zadania nie jest automatycznie sukcesem strategii.

Przy powtarzającym się problemie, odtworzonym błędzie procesu, udokumentowanej nieefektywności mimo DONE albo pasującym kandydacie z pamięci przeczytaj [zasady doskonalenia](references/process-learning.md). Meta-ewaluator analizuje np. braki w briefie, złą dekompozycję, zbędne powtórzenia pracy, konflikty zapisu lub lukę w eval. Nie wyszukuj usprawnień na siłę po każdym sukcesie. Koordynator może automatycznie zastosować zweryfikowaną poprawę lokalnej strategii; zmiana o dużym wpływie wymaga dwóch niezależnych potwierdzeń opisanych w zasadach doskonalenia, bez nowej bramki akceptacji użytkownika.

**Najwyżej jeden kandydat i jeden ograniczony eksperyment porównawczy na wywołanie**, z zachowaniem licznika przy wznowieniu. Nie uruchamiaj eksperymentu bez przydatnego punktu odniesienia. Niedostateczne dane pozostawiają kandydata jako PENDING, nie blokują poprawnie ukończonego zadania. Meta-learning nie daje czwartej próby ani prawa do dodatkowych zmian ukończonego rezultatu.

## Zamknięcie

Kontynuuj autoryzowane prace do wyniku, blokady lub limitu; nie kończ na planie lub samym delegowaniu. Zapisz faktyczny stan i zweryfikowane wnioski. Nowa ręcznie uruchomiona sesja odczytuje właściwą strategię i sprawdza jej skutki.

Raport końcowy: **DONE / NOT_COMPLETED / BLOCKED**, rezultat i odnośniki, wykorzystane próby, dowody dla kryteriów, wersja strategii, wynik meta-eval oraz decyzja o strategii: bez zmiany / PENDING / ACTIVE / REJECTED / ROLLED_BACK. DONE wymaga PASS wszystkich obowiązkowych kryteriów dla zintegrowanego wyniku oraz zapisanej pamięci; nie wymaga udanego eksperymentu. Raport nie zastępuje reguł statusu narzędzia celu.
