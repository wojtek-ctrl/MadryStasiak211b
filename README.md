# MadryStasiak211b
Projekt semestralny z przedmiotu Inżynieria Oprogramowania


Wymagane aplikacje
---
- XAMPP `3.3.0` (PHP `8.0.6`)
- Python `3.8.5`

Wymagane moduły Python
---
- mysql-connector `2.2.9`
- PyQt5 `5.15.1`

Instalacja
---
Po zainstalowaniu `XAMPP` oraz `Python` wraz z jego modułami
odpalamy `XAMPP` i klikamy `Start` odpowiednio przy modułach `Apache`, `MySQL`.

Następnie przechodzimy do zakładki `Admin` przy module `MySQL`.

Klikamy `Nowa` i tworzymy bazę danych, którą nazywamy `inzynieriaoprogramowania`.

Następnie przechodzimy do naszej bazy danych, i klikamy `import`.

Klikamy `Wybierz plik` i wybieramy `inzynieriaoprogramowania.sql` oraz klikamy `Wykonaj`.

Teraz nasza baza danych jest już gotowa du użytku.


Odpalamy plik `database.py` w edytorze tekstowym i zmieniamy dane logowania do bazy na nasze.

Odpalanie
---
Gdy nasza baza danych jest uruchomiona jedyne co musimy, zrobić
to wpisać w `cmd` polecenie `python panel_logowania.py`.