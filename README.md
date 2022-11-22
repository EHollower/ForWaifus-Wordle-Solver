ForWaifus Wordle-Solver
================================================================

Echipa formată din:

- Bucă Mihnea-Vicențiu Grupa 152

- Petrovici Ricardo-Dumitru Grupa 151

------------------------------------------------------------------------------------------------

### Prerequisites


Pentru a putea rula codul va fi nevoie să se instaleze următoarele:

  - [python](https://www.python.org/)

  - [pygame](https://www.pygame.org/news) -> se poate descărca prin comanda:

```
pip install pygame
```
   - [GCC](https://www.geeksforgeeks.org/complete-guide-to-install-c17-in-windows/)
   
   - Fontul găsit în /asstets/font, pentru al instala e neovie să fie instalate toate .ttf file-urile

-----------------------------------------------------------------------------------------------

### How to run

această comandă trebuie rulată o singură dată, odată cu clonarea codului

```
g++ solver.cpp -o solver.exe
```

pentru a rula game.py/shell.py

```
py game.py
or
py shell.py
```

----------------------------------------------------------------------------------------

### Foreword

Procesul de creeare al acestui repo a constiuit o împărțire între creearea interfeței jocului (Bucă Mihnea-Vicențiu) și calculul cuvântului optim de guess(Petrovici Ricardo-Dumitru)

Comentariile codului sunt în **engleză** din motivul că nouă, personal, ne este mai usor să gândim codul și funcționalitățile lui în acest mod. Documentația librăriilor folosite și depanările/google-ingurile ulterioare în urma găsirii unui bug e făcuta în engleză în majoritatea cazurilor

Dacă cumva se găsete un bug/nelămuriri puteți oricănd să dați un email pe adresele noastre de unibuc:

mihnea-vicentiu.buca@s.unibuc.ro
ricardo-dumitru.petrovici@s.unibuc.ro

----------------------------------------------------------------------------------------

### Crearea interfeței jocului / cum interacționează cu solverul 

Bucă Mihnea-Vicențiu

O bună parte din proceseul de creeare al interfaței a fost un "what if" pentru mine, am încercat zeci de posibiliăți, animații, subprocese astfel încat gameul să fie căt mai fluid, mai lipsit de bugguri și cât mai apropiat de originalul wordle de pe NYT. Principalele surse de inspirație au fost [originalul](https://www.nytimes.com/games/wordle/index.html) precum și o [copie](https://wordleunlimited.org/) a lui, pentru a studia mai îndeaproape animațiile/modul de colorare al guessurilor fară sa fiu limitat la un singur cuvânt pe zi.

Pygame nu cred că e, nici pe departe, cea mai bună opțiune pentru a face un joc de wordle, dar am continuat să îl folosec din simplul motiv că sunt cel mai familiar cu bibleoteca și am vrut să reduc pe cât de mult posibil importul de alte bibleoteci grafice/alte module de animații. "All and all" nu a fost nici cel mai ușor lucru, dar nici cel mai greu și sunt destul de mulțumit de rezultatul grafic final al jocului.

Ca structură codul este destul de segmentat și am ales să fie așa, deoarece am încercat pe cât de mult posibil să nu fie un "mumbo jumbo" spaghetti code pe care să nu îl înteleg nici eu la finalul zilei. Fiecare clasă/program în python își au propiul scop, astfel încât dacă la un moment dat mă decid să fac modificări în cod să știu ce, unde și cum am implementat/modificat. Prin aceste procese cred că am reușit destul de mult să fac codul cât mai citibil pentru toată lumea.

Solverul a fost scirs de **Petrovici Ricardo-Dumitru**, dar am contribuit și acolo prin restructureare codului într-o maniera destul de diferită față de cum scriem codul C++ de obicei. Am vrut să simplificăm cât mai mult procesul de link între joc și solver, astfel încât să fie nevoie de cât mai puțin cod/bibleoteci. Am ales să scriem solverul in C++ deoarece, suntem foarte familiari cu limbajul (fiind amândoi olimpici la info în liceu) și pentru a găsi și a trimite outputul optim într-un timp scurt.

Descrierea mai îndetaliu a proceselor se află în cod, deși este în engleză, din motive pe care le-am enunțat mai sus, cred că sunt destul de clar descrise implementările programelor/claselor/animațiilor, dar ca **TLDR**: jocul și solverul comunică printr-un fișier "communication.txt" care va fi creat la rularea jocului/solverului, ambele programe furnizând unul celuilalt oputut/input în funcție de informațiile primite.

----------------------------------------------------------------------------------------

### Calculul entropiei

Petrovici Ricardo-Dumitru

Lista completă de soluții la toate cuvintele este in fișierul "solutii.txt"

Soluția ne-a oferit un număr mediu al guessurilor de $3.98979$.

Ideea de calcul al cuvântului optim pe care îl ghicim este următoarea: putem observa că guess-ul nostru poate fi în maxim $243$ de situați posibile față de cuvântul pe care trebuie să îl ghicim, asta ne dă ideea de a lua un cuvânt(pentru simplitate o să îl notăm cu A), apoi să interăm prin toate cuvintele din mulțime și să contorizăm în ce raport se află A dacă i-am da guess, iar cuvintele din mulțime ar fi pe rând cuvântul care trebuie ghicit. Apoi pentru a obține cantitatea de informație pe care un cuvânt ni-l oferă interăm prin toate paternele și folosim formula  $S$ = $\frac{P_0}{n}$ * $log_2(\frac{n}{P_0})$ + $\frac{P_1}{n}$ * $log_2(\frac{n}{P_1})$ $+ ...... +$ $\frac{P_{242}}{n}$ * $log_2(\frac{n}{P_{242}})$, unde $P_k$ reprezintă numărul de apariți al paternului $k$, iar $n$ reprezintă numărul de cuvinte din mulțime, repetăm acest lucru pentru fiecare cuvănt și astfel aflăm cuvântul optim. După acesti pași mai rămâne să restrângem mulțimea doar la cuvintele care ne oferă același patern în raport cu cuvântul care trebuie ghicit, ca cel oferit de guess, apoi repetăm procedeul cautăm iarăși cuvântul optim în mulțimea restrânsă. Această soluție ne oferă un număr mediu al guess-uri de $4.37367$(inculde și guessul final când ghicim cuvântul respectiv).

Deși bună soluția precedentă ne creează câteva cazuri nasoale, un exemplu find: VOTUL TAREI COTUL BOTUL FOTUL GOTUL HOTUL LOTUL MOTUL POTUL SOTUL VOTUL $11$, aici toate cuvintele din mulțimea restrânsă ne oferă foarte puțină informație. O soluție ar fi să nu căutăm cuvântul optim doar în mulțimea restrânsă, ci în toată mulțimea cuvintelor. Această soluție ne crează următoarea problemă, atunci cănd toate cuvintele se restrâng la un patern foarte precis putem avea multe cuvinte care sunt optime, dar să alegem unul care în practică ne oferă $0$ biți de informație și crează o buclă infinită. Această problemă poate fi rezolvată dacă mereu ținem mulțimea cuvintelor optime la începutul arrayul de cuvinte, astfel obținem un număr mediu al guessurilor de $3.98979$(obținut cu deschiderea "TAREI"), dar este în medie de $30$ de ori mai lentă.

 O altă soluție posibil mai bună(nu a fost implementantă):
 
Putem observa că ținem cont doar de stadiul actual, fară să vedem și cum se comportă paternele în care ne împarte cuvăntul optim mulțimea noastră, astfel cuvântul optim obținut nu este mereu optim, de exemplu la calculul pe mulțimea inițială ne-a dat că "TAREI" este deschiderea optimă, dar în practică "CARTE"(în situația în care "TAREI ne-a oferit un număr mediu al guessurilor de $4.37$, "CARTE" ne-a oferit $4.30$), astfel ne vine ideea de a cacula cuvântul cu adevărat optim, apoi să repetăm procesul pentru fiecare patern al cuvântului, astfel aflând de fiecare dată cuvântul cu adeverăt optim, dar această soluție este extrem de lentă în practică și ne creează câteva milioane de instanțe posibile, putem salva toate aceste instanțe într-un fișier și doar să îl citim la începutul programului, astfel precalculând toate rezultatele și necesitănd doar un calcul inițial foarte mare, bine înteles ar fi tot mai lentă ca soluția actuală, citirea datelor durând mai mult decât rularea soluției actuale.

----------------------------------------------------------------------------------------

### Referinte

[orginialul wordle game](https://www.nytimes.com/games/wordle/index.html)

[copia wordle game](https://wordleunlimited.org/)

[Solving Wordle using information theory](https://www.youtube.com/watch?v=v68zYyaEmEA&t=0s)

[Oh, wait, actually the best Wordle opener is not “crane”…](https://www.youtube.com/watch?v=fRed0Xmc2Wg&t=0s)

[Maximising Differential Entropy to Solve Wordle](https://aditya-sengupta.github.io/coding/2022/01/13/wordle.html)

[Intuitively Understanding the Shannon Entropy](https://www.youtube.com/watch?v=0GCGaw0QOhA)

[Entropy in Compression - Computerphile](https://www.youtube.com/watch?v=M5c_RFKVkko)
