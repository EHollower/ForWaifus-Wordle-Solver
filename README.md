ForWaifus Wordle-Solver
================================================================

Echipa formata din:

- Bucă Mihnea-Vicențiu Grupa 152

- Petrovici Ricardo-Dumitru Grupa 151

------------------------------------------------------------------------------------------------

### Prerequisites


Pentru a putea rula codul va fi nevoie sa se intaleze urmatoarele:

  - [python](https://www.python.org/)

  - [pygame](https://www.pygame.org/news) -> se poate va descarca prin comanda:

```
pip install pygame
```
   - [GCC](https://www.geeksforgeeks.org/complete-guide-to-install-c17-in-windows/)

-----------------------------------------------------------------------------------------------

### How to run

aceasta comanda trebuie rulata o singura data odata cu clonarea codului

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

Procesul de creeare al acestui repo a constiuit o impartire intre creearea interfetiei jocului (Bucă Mihnea-Vicențiu) si calculul cuvantului optim de guess(Petrovici Ricardo-Dumitru)

Comentariile codului sunt in **engleza** din motivul ca noua, personal, ne este mai usor sa gandim codul si functionalitatile lui in acest mod. Documentatia librariilor folosite si depanarile/google-ingurile ulterioare in urma gasirii unui bug e facuta in engleza in majoirtatea cazurilor

Daca cumva se gasete un bug/nelamuriri puteti oricand sa dati un email pe adresele noastre de unibuc:

----------------------------------------------------------------------------------------

### Crearea interfetei jocului / cum interactioneaza cu solverul (Bucă Mihnea-Vicențiu)

O buna parte din proceseul de creeare al interfatei a fost un "what if" pentru mine, am incercat zeci de posibiliati, animatii, subprocese astfel incat gameul sa fie cat mai fluid, mai lipsit de bugguri si cat mai apropiat de originalul wordle de pe NYT. Principalele surse de inspiratie a fost [originalul](https://www.nytimes.com/games/wordle/index.html) precum si o [copie](https://wordleunlimited.org/) al lui, pentru a studia mai indeaproape animatiile/modul de colorare al guessurilor fara sa fiu limitat la un singur cuvant pe zi.

Pygame nu cred ca e, nici pe departe, cea mai buna obtiune pentru a face un joc de wordle, dar am continuat sa il folosec din simplul motiv ca sunt cel mai familiar cu bibleoteca si am vrut sa reduc pe cat de mult posibil importul de alte bibleoteci grafice/alte module de animatii. "All and all" nu a fost nici cel mai usor lucru, dar nici cel mai greu si sunt destul de multumit de rezultatul grafic final al jocului.

Ca structura codul este desutl de segmentat si am ales sa fie asa, deoarece am incercat pe cat de mult posibil sa nu fie un "mumbo jumbo" spaghetti code pe care sa nu il inteleg nici eu la finalul zilei. Fiecare clasa/program in python isi au propiul scop, astfel incat daca la un moment dat ma decid sa fac modificari in cod sa stiu ce, unde si cum am implementat/modificat. Prin aceste procese cred ca am reusit destul de mult sa fac codul cat mai citibil pentru toata lumea.

Solverul a fost scirs de **Petrovici Ricardo-Dumitru**, dar am contribuit si acolo prin restructureare codului intr-o maniera destul de diferita fata de cum scriem codul C++ de obicei. Am vrut sa simplificam cat mai mult procesul de link intre joc si solver, astfel incat sa fie nevoie de cat mai putin cod/bibleoteci. Am ales sa scriem solverul in C++ deoarece, suntem foarte familiari cu limbajul (fiind amandoi olimpici la info in liceu),si entru a gasi si a timite outputul optim intr-un timp scurt.

Descrierea mai indetaliu a proceselor se afla in cod, desi este in engleza, din motive pe care le-am enuntat mai sus, cred ca sunt destul de clar descrise implementarile programelor/claselor/animatiiolor, dar ca *TLDR*: jocul si solverul comunica printr-un fisier "communication.txt" care va fi creat la rularea jocului/solverului, ambele programe furnizand una celeilalte oputut/input in functie de informatiile primite.

----------------------------------------------------------------------------------------

### Calculul entropiei

Petrovici Ricardo-Dumitru

Solutia ne-a oferit un numar mediu al guess-urilor de $3.98979$.

Ideea de calcul al cuvantului optim pe care il ghicim este urmatoarea: putem observa ca guess-ul nostru poate fi in maxim $243$ de situati posibil fata de cuvantul pe care trebuie sa il ghicim, asta ne da ideea de a lua un cuvant(pentru simplitate o sa il notam cu A), apoi sa interam prin toate cuvintele din multime si sa contorizam in ce raport se afla A daca i-am da guess, iar cuvintele din multime ar fi pe rand cuvantul care trebuie ghicit. Apoi pentru a obtine cantitatea de informatie pe care un cuvant ni-l ofera interam prin toate paternele si folosim formula  $S$ = $\frac{P_0}{n}$ * $log_2(\frac{n}{P_0})$ + $\frac{P_1}{n}$ * $log_2(\frac{n}{P_1})$ $+ ...... +$ $\frac{P_{242}}{n}$ * $log_2(\frac{n}{P_{242}})$, unde $P_k$ reprezinta numarul de apariti al paternului $k$, iar $n$ reprezinta numarul de cuvinte din multime, repetam acest lucru pentru fiecare cuvant si astfel aflam cuvantul optim. Dupa acesti pasi mai ramane sa restrangem multimea doar la cuvintele care ne ofera acelasi patern in raport cu cuvantul care trebuie ghicit, ca cel oferit de guessul oferit, apoi repetam procedeul cautam iarasi cuvantul optim in multimea restransa. Aceasta solutie ne ofera un numar mediu al guess-uri de $4.37367$(inculde si guessul final cand ghicim cuvantul respectiv).

Desi buna solutia precedenta ne creeaza cateva cazuri nasoale, un exemplu find: VOTUL TAREI COTUL BOTUL FOTUL GOTUL HOTUL LOTUL MOTUL POTUL SOTUL VOTUL $11$, aici toate cuvintele din multimea restransa ne ofera foarte putina informatie. O solutie ar fi sa nu cautam cuvantul optim doar in multimea restransa, ci in toata multimea cuvintelor. Aceasta solutie ne creaza urmatoarea problema, atunci cand toate cuvintele se restrang la un patern foarte precis putem avea multe cuvinte care sunt optime, dar sa alegem unu care in practica ne ofera doar $0$ biti de informatie si creaza o bucla infinita. Aceasta problema poate fi rezolvata daca mereu tine multimea cuvintelor optime la inceputul array-ul din cuvinte, astfel obtinem un numar mediu al guess-urilor de $3.98979$(obtinut cu deschiderea "TAREI"), dar este in medie de 30 de ori mai lenta.

 O alta solutie posibil mai buna(nu a fost implementanta):
 
Putem observa ca tinem cont doar de stadiul actual curent, fara sa vedem si cum se comporta paterne in care ne imparte cuvantul optim multimea noastra, astfel cuvantul optim obtinut nu este mereu, de exemplu la calculul pe multimea initiala ne-a dat ca "TAREI" este deschiderea optima, dar in practica "CARTE"(in situatia in care "TAREI ne-a oferit un numar mediu al guess-uri de $4.37$, "CARTE" ne-a oferit $4.30$), astfel ne vine ideea de a cacula cuvantul cu adevarat optim, apoi sa repetam procesul pentru fiecare patern al cuvantului, astfel afland de fiecare data cuvantul cu adeverat optim, dar aceasta solutie este extrem de lenta in practica si ne creeaza cateva milioane de instante posibil, putem salva toate aceste instanta intr-un fisier si doar sa il citim la inceputul programului, astfel precalculand toate rezultatele si necesitand doar un calcul initial foarte mare, bine inteles ar fi tot mai lenta ca solutia initiala, citirea datelor durantd mai mult decat rularea solutiei actuale.
