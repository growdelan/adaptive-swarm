# Doskonalenie strategii

Celem jest udokumentowana poprawa decyzji organizacyjnych w danym projekcie. Oddziel efekt procesu od zmiany kodu, modelu, kryteriów czy trudności zadania. Nie przypisuj poprawy strategii tylko dlatego, że kolejna próba zakończyła się PASS.

## Od diagnozy do kandydata

Meta-ewaluator analizuje rzeczywiste dowody: kontrakt, briefy, podział pracy, użyte wersje strategii, wyniki eval i wcześniejsze pasujące doświadczenia. Odróżnia przyczynę od korelacji. Błąd środowiska nie uzasadnia automatycznie nowej roli; brak sygnału kończy meta-eval bez zmiany.

Przy potwierdzonym, powtarzającym się błędzie rozważ trwałe zabezpieczenie w projekcie: test regresyjny, regułę lintowania lub ograniczenie interfejsu, zamiast kolejnej notatki. Wybierz rozwiązanie proporcjonalne do problemu, bez obowiązkowej przebudowy architektury. Zmiana kodu, testów lub CI jest zmianą rezultatu projektu, nie samą strategią: wykonuj ją tylko w autoryzowanym zakresie, z odpowiednią weryfikacją i zachowaniem limitu prób. Po DONE albo wyczerpaniu prób zapisz propozycję bez wykonywania dodatkowych zmian produktu. Sprawdzenie działania zabezpieczenia nie dowodzi korzyści strategii; jej promocja nadal wymaga porównania opisanego poniżej.

Sygnałem może być także nieefektywność przy DONE: np. zapisane powtórzenia identycznej pracy bez nowej potrzeby, agent bez wykorzystanego rezultatu lub zmierzony koszt przekraczający ustalony cel. Samo odczucie, że zadanie trwało długo, nie wystarcza. Wskaż konkretny ślad i zachowaj kryteria jakości. Bez pomiarów czasu lub tokenów nie deklaruj ich oszczędności; jeśli są dowody powtórzeń, można mierzyć ich liczbę. Ocena procesu nie zmienia PASS dostarczonego wyniku i nie uruchamia automatycznie eksperymentu po każdym sukcesie.

Kandydat zmienia **jedną sprawdzalną decyzję procesu**, np. rozpoznanie granic modułu przed implementacją, zakres briefu, kolejność dwóch prac, dobór modelu dla lekkiego podzadania, wybór effort lub dodatkowy przypadek weryfikacji. Dobór modelu musi respektować granice ze SKILL.md, w tym Sol 6.1 do eval i meta-eval. Model albo effort może różnić warianty tylko wtedy, gdy jest jedyną badaną zmianą; w pozostałych porównaniach utrzymaj oba bez zmian. Nie musi to oznaczać nowego agenta. W PROJECT.md zapisz:

- ID, wersję bazową, zakres zastosowania, konkretną zmianę oraz mały/duży wpływ z uzasadnieniem;
- obserwację z dowodem oraz przewidywany mechanizm poprawy;
- miarę główną, kierunek poprawy, próg akceptacji i dopuszczalny koszt;
- chronione kryteria jakości i regresje, które dyskwalifikują wariant;
- plan porównania, punkt odniesienia, warunek rollbacku i status PENDING.

Ustal je przed zobaczeniem wyników. Wniosek „zawsze dodawaj Architecture Scout” jest zbyt szeroki, jeśli dowód dotyczy jednego modułu. Ogranicz regułę do sytuacji, dla których istnieje uzasadnienie.

Zmiana ma duży wpływ, jeśli obejmuje szeroką klasę przyszłych zadań, stale zwiększa zasoby lub istotnie zmienia podział odpowiedzialności bądź sposób weryfikacji. Drobna, odwracalna korekta briefu w wąskim zakresie może mieć mały wpływ. Klasyfikacji nie obniżaj po wyniku tylko po to, aby przyspieszyć promocję.

## Ograniczony eksperyment

Na wywołanie przeprowadź najwyżej jedno porównanie **A = bieżąca strategia, B = kandydat**, bez dostrajania B po poznaniu wyniku. Wybierz jedną metodę:

- **Kontrolowane odtworzenie:** ten sam utrwalony punkt startowy, input, kontrakt, zasoby i porównywalny budżet dla A i B; izolowane kopie lub bezpieczna próba tylko do odczytu. Sprawdź znany przypadek oraz pasujący przypadek nieużyty do zaprojektowania zmiany, jeśli jest dostępny.
- **Obserwacja w kolejnych ręcznie zleconych zadaniach:** zaplanuj porównywalną klasę zadań i z góry warunki porównania; zapisz istotne różnice oraz inne zmiany. Do czasu wystarczających dowodów kandydat pozostaje PENDING. Jednorazowe zastosowanie w zadaniu oznacz jawnie jako próbę, nie aktywną regułę.

Nie porównuj starego błędnego produktu z poprawionym produktem jako dowodu przewagi procesu. Gdy obydwu wariantów nie można porównać uczciwie lub nie ma miarodajnego kosztu, użyj dostępnych miar i ujawnij brak danych; nie zgaduj oszczędności tokenów lub czasu. Jeśli eksperyment nie jest wykonalny, odłóż go bez zastępowania pomiaru opinią agenta.

Przydatne miary to np. przeoczenia wykryte na utrwalonych przypadkach, konflikty edycji, spełnione kryteria po pierwszej próbie lub rzeczywiście zmierzony czas. Więcej testów czy agentów nie jest samo w sobie poprawą. Ogranicz czas lub liczbę operacji wariantów przed startem; ten sam limit dotyczy A i B. Osiągnięcie limitu daje niepełny wynik, nie dodatkową rundę eksperymentu.

Eksperyment nie może odtwarzać nieodwracalnych działań w systemach zewnętrznych. Wykorzystuj izolowane, odwracalne próbki. Zmiana właściwego rozwiązania po FAIL zawsze zużywa kolejną z trzech prób, także gdy nazwano ją eksperymentem. Po wykorzystaniu trzech prób dopuszczalna jest analiza i zapis kandydata, nie dalsze wykonanie ani eksperymentalna naprawa tego celu. Po DONE nie zmieniaj ukończonego rezultatu; dopuszczalny jest wyłącznie ograniczony eksperyment na izolowanej próbce.

## Ocena, promocja i rollback

Porównanie ocenia agent, który nie stworzył kandydata ani ocenianych rezultatów. Może to być dotychczasowy ewaluator, jeśli spełnia tę niezależność. Sam sprawdza dowody, porównywalność i nienaruszenie kryteriów; nie akceptuje deklarowanego zwycięstwa wykonawcy. Zewnętrzne lub nieobserwowalne kryteria pozostają UNVERIFIED.

Dla małego wpływu wystarcza jedno poprawne potwierdzenie. Dla dużego wpływu wymagaj dwóch: pierwszego porównania i drugiego potwierdzenia przewidywanego efektu na innym, pasującym przypadku, nieużytym do opracowania zmiany. Każde musi spełnić ustalone progi jakości, korzyści i kosztu oraz uzyskać niezależną ocenę; ponowny odczyt tej samej próby przez innego agenta nie jest drugim dowodem. Samo DONE kolejnego zadania również nie wystarcza.

Drugie potwierdzenie zbierz w następnym, ręcznie zleconym pasującym zadaniu, bez obchodzenia limitu jednego eksperymentu i trzech prób. Do tego czasu kandydat pozostaje PENDING z zapisem np. „1 z 2 potwierdzeń”, a aktywna strategia się nie zmienia. Zastosowanie kandydata na potrzeby drugiego porównania oznacz jako ograniczoną próbę. Dwa potwierdzenia są warunkiem operacyjnym, nie statystyczną gwarancją. Brak dotychczasowej klasyfikacji lub dowodów w starej pamięci nie pozwala ich domniemywać; sklasyfikuj kandydata i zweryfikuj istniejące dowody przed promocją. Nie cofaj automatycznie historycznych aktywnych strategii tylko z powodu aktualizacji skilla.

- **PENDING:** brak porównania, nieporównywalne dane, niepełne sprawdzenie, niepewny efekt lub brak wymaganego drugiego potwierdzenia. Nie zastępuje aktywnej strategii.
- **ACTIVE:** uzyskano liczbę potwierdzeń wymaganą dla wpływu zmiany, spełniono uprzednie progi poprawy i kosztu, bez naruszenia jakości. Koordynator zapisuje nową wersję S1, S2… oraz poprzednią działającą wersję i stosuje nową regułę tylko w potwierdzonym zakresie. Bez przypadku sprawdzającego uogólnienie zakres pozostaje ograniczony do odtworzonej sytuacji.
- **REJECTED:** ukończone, porównywalne sprawdzenie nie spełniło progu korzyści, przekroczyło limit kosztu lub ujawniło regresję. Zachowaj powód; nie próbuj kolejnego wariantu w tym wywołaniu.
- **ROLLED_BACK:** późniejsze dowody spełniły warunek wycofania. Przywróć zapisaną poprzednią sprawdzoną strategię, odnotuj wersję i dowód. Rollback strategii nie cofa zmian użytkownika i nie daje nowych prób naprawy rezultatu.

Nie traktuj braku danych jako FAIL kandydata ani pojedynczego lokalnego sukcesu jako statystycznej gwarancji. Przed kolejnym użyciem sprawdź, czy zakres i przesłanki nadal pasują. Monitoruj rzeczywisty efekt i koszt w następnych zadaniach; wycofaj regułę przy potwierdzonej regresji lub sprzeczności z aktualnym kontraktem. Bez pasującego zadania efekt pozostaje niezmierzony.

Zmienia się strategia w PROJECT.md, briefy i decyzje wykonania, a nie chroniony rdzeń skilla. Meta-learning nie może rozszerzyć listy dozwolonych modeli ani przekazać Lunie 6 roli wymagającej Sol 6.1. Nie może zmienić ręcznego startu, limitu trzech prób, czterech plików, uprawnień, niezależności oceny ani kryteriów użytkownika. Nie przechodź samodzielnie do kolejnego celu, nie twórz rekurencyjnych zespołów i nie przepisuj globalnego skilla pod lokalne doświadczenie.
