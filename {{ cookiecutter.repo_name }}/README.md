# {{cookiecutter.project_name}}
---

{{cookiecutter.description}}

## Project Organization
---

```
{% if cookiecutter.project_size == "Small" %}ROOT:.
│   LICENSE
│   .gitignore             <- Plik definiujący, które pliki nie mogą być wysyłane do repozytorium
│   README.md              <- Wysoko-poziomowy plik opisujący projekt
│   requirements.txt       <- Plik pozwalający na reprodukcje wirtualnego środowiska używanego w projekcie
│   setup.py               <- Plik pozwalający na instalowanie modułu src z użyciem `pip install`
│
├───data                   <- Folder do przechowywania danych
│
├───media                  <- Folder na zdjęcia, obrazy, wykresy, gify itd.
│
├───models                 <- Folder do zapisywania modeli
│
├───src                    <- Folder na cały kod wykorzystywany w projekcie
│   │   consts.py          <- Plik przechowujący zmienne globalne/ustawienia w projekcie, 
│   │                         np. ścieżki do plików, pisane capslockiem
│   │   __init__.py        <- Sprawia, że src staje się modułem{% elif cookiecutter.project_size == "Medium" %}ROOT:.
│   LICENSE
│   .gitignore             <- Plik definiujący, które pliki nie mogą być wysyłane do repozytorium
│   README.md              <- Wysoko-poziomowy plik opisujący projekt
│   requirements.txt       <- Plik pozwalający na reprodukcje wirtualnego środowiska używanego w projekcie
│   setup.py               <- Plik pozwalający na instalowanie modułu src z użyciem `pip install`
│
├───data
│   ├───interim            <- Dane w standardzie "srebrnym", czyli po procesowaniu
│   │
│   ├───processed          <- Dane w standardzie "złotym", czyli ostateczne
│   │
│   └───raw                <- Dane w standardzie "brązowym", czyli w stanie surowym
│
├───media                  <- Folder na zdjęcia, obrazy, wykresy, gify itd.
│
├───models                 <- Folder do zapisywania modeli
│
├───notebooks              <- Jupyter notebooks. Nazywamy w konwencji liczba (dla sortowania), autor i krótki
│   │                         opis oddzielony `_`, np. `1.0_rs_procesowanie_danych.ipynb`
│   ├───draft              <- Folder, z Jupyter Notebook'ami będącymi brudnopisami 
│
├───src                    <- Folder na cały kod wykorzystywany w projekcie
│   │   consts.py          <- Plik przechowujący zmienne globalne/ustawienia w projekcie, 
│   │                         np. ścieżki do plików, pisane capslockiem
│   │   __init__.py        <- Sprawia, że src staje się modułem
│   │
│   ├───data               <- Skrypty do generowania/procesowania danych
│   │
│   ├───models             <- Skrypty do modelowania
│   │
│   └───visualization      <- Skrypty do wizualizacji wyników
│
└───tests                  <- Skrypty testujące projekt{% elif cookiecutter.project_size == "Large" %}ROOT:.
│   LICENSE
│   .env                   <- Plik do przechowywania zmiennych poufnych 
│   .gitignore             <- Plik definiujący, które pliki nie mogą być wysyłane do repozytorium
│   Makefile               <- Plik pozwalające definiować komendy z użyciem `make`
│   README.md              <- Wysoko-poziomowy plik opisujący projekt
│   requirements.txt       <- Plik pozwalający na reprodukcje wirtualnego środowiska używanego w projekcie
│   setup.py               <- Plik pozwalający na instalowanie modułu src z użyciem `pip install`
│
├───data
│   ├───interim            <- Dane w standardzie "srebrnym", czyli po procesowaniu
│   │
│   ├───processed          <- Dane w standardzie "złotym", czyli ostateczne
│   │
│   └───raw                <- Dane w standardzie "brązowym", czyli w stanie surowym
│
├───docs                   <- Folder na przechowanie dokumentacji
│
├───media                  <- Folder na zdjęcia, obrazy, wykresy, gify itd.
│
├───models                 <- Folder do zapisywania modeli
│
├───notebooks              <- Jupyter notebooks. Nazywamy w konwencji liczba (dla sortowania), autor i krótki
│   │                         opis oddzielony `_`, np. `1.0_rs_procesowanie_danych.ipynb`
│   ├───draft              <- Folder, z Jupyter Notebook'ami będącymi brudnopisami 
│
├───src                    <- Folder na cały kod wykorzystywany w projekcie
│   │   consts.py          <- Plik przechowujący zmienne globalne/ustawienia w projekcie, 
│   │                         np. ścieżki do plików, pisane capslockiem
│   │   __init__.py        <- Sprawia, że src staje się modułem
│   │
│   ├───data               <- Skrypty do generowania/procesowania danych
│   │
│   ├───models             <- Skrypty do modelowania
│   │
│   └───visualization      <- Skrypty do wizualizacji wyników
│
└───tests                  <- Skrypty testujące projekt{% endif %}
```

---