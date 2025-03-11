Projekt bol originalne pre jeden pivovar ktorý ma 2 pobočky ale po tom čo dizajner opustil projekt sa to nikam dalej nedostalo, kazdopadne miesto pobočky som tam dal 2 vodne plochy v bratislave a miesto obrazkov a videií z pobočiek su tam stockimages a fotky zvieratiek. Dizajn som bohuzial robil ja sam, takze to aj tak vyzera ale najhoršie to hadam neni. Media je pomerne jednoduche vymenit.

Treba mat pip, python 3.9., git, Virtual Environment napr. v pythone venv 

Otvort terminál a nakopiruj z gitu
Vytvort virtuálne prostredie s názvom .venv:

python -m venv .venv

Aktivuj virtuálne prostredie:

Windows:
.venv\Scripts\activate

macOS/Linux:
source .venv/bin/activate

Aplikovanie migrácie
Vytvor a nastav databázu:

python manage.py migrate

Vytvorenie superusera

Ak chceš získať prístup do administrátorskeho rozhrania Django, treba mat superusera:

python manage.py createsuperuser

Postupujte podľa pokynov a zadajte užívateľské meno, e-mail a heslo.

Spustenie development servera
python manage.py runserver

Prístup do administrátorského rozhrania
Prihlás sa do administrácie http://127.0.0.1:8000/admin/ pomocou superuser

Predvolená databáza je SQLite (db.sqlite3).

Statické súbory – Pre produkčné prostredie spustit:

python manage.py collectstatic

Environment variables – Pre citlivé nastavenia (napr. tajný kľúč, prístupy k databáze) použite environment variables alebo .env súbor.

Na server som to nenahadzoval ešte... comming soon 
