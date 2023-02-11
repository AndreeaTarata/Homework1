Principii de baza în programare

● A compila = a traduce din ‘human reading syntax’ în ‘machine language’
● Codul se interpretează secvențial, linie cu linie, de sus în jos
● Machine language = binary code (cod binar) - combinații diferite de 0 și 1
● Principiul seamănă cu cel din codul morse. Pt 1 se transmite un impuls electric, pt 0 o pauză.
● 1 bit = memorie în care încape doar o singură valoare. 1 (true), 0 (false)
● 1 Byte = 8 biți. Numere între 0 (00000000) și 255 (11111111)
● 1 Kilobyte = 1.024 bytes
● 1 Megabyte = 1.024 kilobytes (1.048.575 bytes)
● Terminal - zona în care trimitem instrucțiuni către program - altele decât cod python
○ Ex: ‘python – version’
○ Tot de aici putem instala librării externe (ex: pip install selenium)
● Consola - zona în care primim output (răspuns vizual) de la programul rulat
● IDE - Integrated Development Environment - Pycharm. Este un editor de cod
● Venv - Virtual environment - zona care folosesc în mod izolat și securizat toate librăriile externe

Hello World + Comentarii

Variabile

● O variabilă este un container din memorie care stochează valori.
● Îți poți imagina o cutiuță pe care punem un label.
● Variabilele au nume unic că să poată fi identificate și folosite ulterior.
● Variabila e creată în momentul în care îi atribuim o valoare.
● Nu putem pune spațiu în numele unei variabile (my_var sau myVar).
● Variabilele încep cu litera mică dar pot conține cifre (user1) și simbolul _ .
● Variabilele sunt case sensitive (myvar=3 e diferită de myVar=5).
● Variabilele pot să își schimbe valoarea pe parcursul execuției programului (suprascriere).
○ Și chiar și tipul de date
● Putem atribui mai multe valori in one line, sau aceeași valoare mai multor variabile.

Tipuri de date

● Datele salvate în variabile pot avea diferite tipuri.
● Există mai multe tipuri de date, dar cele mai importante/ folosite sunt:
○ int - număr întreg;
○ float - număr zecimal;
○ bool - adevărat/fals;
○ string - șir de caractere de la tastatură delimitate de ‘ ‘ sau “ “ .
● În întâlnirea 3 vom discuta și despre colecții, care sunt toate tipurile de date (list, dict, set, tuple).

Funcția type() și type casting

● O funcție este o logică de cod predefinită care face ceva.
● Are sintaxa nume_functie().
● În paranteze punem datele de intrare / input.
● Vom discuta pe larg despre funcții în capitolele următoare.
● Funcția type ne expune tipul de date al variabilei date că input.

● Funcțiile int(), str(), bool(), float() schimbă tipul de date. (ex: int(‘3’) => 3)

Funcția print()

● Printează în consolă ce punem între paranteze.
● Dacă dorim să facem o concatenare (adunare) de stringuri, putem face asta cu +.

● Dacă dorim să adunăm int + string (mere cu pere), vom primi eroare.
● Exista 2 soluții pentru a rezolva această problemă.

Assert

● Assert e o modalitate de a face verificări în programare.
● Verifică dacă statement (propoziția) este evaluată în final că True.
● Dacă răspunsul e True, codul curge mai departe.
● Dacă răspunsul e False, codul se oprește și dă o eroare. Nu se execută liniile de cod ce urmează.
● Toate testele automate se termină în mod normal cu un assert, deci cu o verificare.

Funcția input()

● Funcția input() ne ajută să luăm date de la tastatură și să le salvăm într-o variabilă.
● Dacă nu facem type casting, defaultul datelor date de user = string.
● Ulterior putem accesa valorile salvate în variabile după necesitate.

String (index, len(), slicing, metode)
● Fiecare caracter dintr-un string, are un număr asociat (index), începând de la 0.
● Funcția len() ne spune câte caractere are stringul.
● Slicing - putem accesa ‘felii’ din string folosind următoarea sintaxă:
○ My_str[start_pos, end_pos, pas]
● După my_str dacă punem . ajungem la funcții ajutătoare:
○ Upper, lower, replace, count etc.
○ Accesați descrierea lor apăsând CTRL+Click pe numele lor.

Întrebări & curiozități?
Întrebări de interviu:

➢ Ce este o variabila?
➢ Care sunt cele mai importante tipuri de date?
➢ Când folosim funcția type()?