# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wrd",
    version="1.0.0",
    author="Claude Code User",
    author_email="user@example.com",
    description="WRD (Word) - Narzędzie workflow dla Claude Code na Fedorze",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/wrd",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "rich>=12.0.0",
        "pydantic>=1.9.0",
        "python-dotenv>=0.19.0",
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
        "data": [
            "pandas>=1.5.0",
            "numpy>=1.24.0",
            "matplotlib>=3.6.0",
        ],
        "web": [
            "fastapi>=0.95.0",
            "uvicorn>=0.20.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "wrd=wrd.cli:main",
            "word=wrd.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "wrd": ["templates/*", "configs/*"],
    },
)

# ---

# pyproject.toml
[build - system]
requires = ["setuptools>=45", "wheel"]
build - backend = "setuptools.build_meta"

[project]
name = "wrd"
version = "1.0.0"
description = "WRD (Word) - Narzędzie workflow dla Claude Code na Fedorze"
readme = "README.md"
license = {text = "MIT"}
authors = [
    {name = "Claude Code User", email = "user@example.com"}
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Operating System :: POSIX :: Linux",
]
requires - python = ">=3.8"
dependencies = [
    "click>=8.0.0",
    "rich>=12.0.0",
    "pydantic>=1.9.0",
    "python-dotenv>=0.19.0",
    "requests>=2.28.0",
]

[project.optional - dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "flake8>=4.0.0",
    "mypy>=0.950",
]
data = [
    "pandas>=1.5.0",
    "numpy>=1.24.0",
    "matplotlib>=3.6.0",
]
web = [
    "fastapi>=0.95.0",
    "uvicorn>=0.20.0",
]

[project.scripts]
wrd = "wrd.cli:main"
word = "wrd.cli:main"

[project.urls]
Homepage = "https://github.com/username/wrd"
Documentation = "https://github.com/username/wrd#readme"
Repository = "https://github.com/username/wrd.git"
"Bug Tracker" = "https://github.com/username/wrd/issues"

[tool.black]
line - length = 88
target - version = ['py38']
include = '\.pyi?

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

---

# requirements.txt
click >= 8.0
.0
rich >= 12.0
.0
pydantic >= 1.9
.0
python - dotenv >= 0.19
.0
requests >= 2.28
.0

---

# requirements-dev.txt
-r
requirements.txt
pytest >= 7.0
.0
black >= 22.0
.0
flake8 >= 4.0
.0
mypy >= 0.950
pre - commit >= 2.20
.0

---

# Makefile
.PHONY: install
install - dev
test
lint
format
clean
build
upload
help

# Domyślny target
help:


@echo


"WRD (Word) - Dostępne komendy:"


@echo


"  install     - Instalacja podstawowych zależności"


@echo


"  install-dev - Instalacja zależności deweloperskich"


@echo


"  test        - Uruchomienie testów"


@echo


"  lint        - Analiza kodu (flake8, mypy)"


@echo


"  format      - Formatowanie kodu (black)"


@echo


"  clean       - Czyszczenie plików tymczasowych"


@echo


"  build       - Budowanie pakietu"


@echo


"  upload      - Upload do PyPI"


@echo


"  setup-fedora - Konfiguracja środowiska na Fedorze"

install:
pip
install - r
requirements.txt

install - dev:
pip
install - r
requirements - dev.txt
pip
install - e.

test:
pytest
tests / -v

lint:
flake8
wrd /
mypy
wrd /

format:
black
wrd / tests /
isort
wrd / tests /

clean:
rm - rf
build /
rm - rf
dist /
rm - rf *.egg - info /
find. - type
d - name
__pycache__ - delete
find. - type
f - name
"*.pyc" - delete

build: clean
python - m
build

upload: build
python - m
twine
upload
dist / *

setup - fedora:


@echo


"🔧 Konfiguracja WRD na Fedorze..."
sudo
dnf
install - y
python3 - pip
python3 - venv
git
python3 - m
venv
~ /.wrd - env
source
~ /.wrd - env / bin / activate & & pip
install - -upgrade
pip
setuptools
wheel


@echo


"✅ Środowisko przygotowane"


@echo


"Aktywuj środowisko: source ~/.wrd-env/bin/activate"


@echo


"Następnie uruchom: make install-dev"

---

# MANIFEST.in
include
README.md
include
LICENSE
include
requirements.txt
include
requirements - dev.txt
include
Makefile
recursive - include
wrd / templates *
recursive - include
wrd / configs *
recursive - exclude * __pycache__
recursive - exclude * *.py[co]

---

# .gitignore
# Byte-compiled / optimized / DLL files
__pycache__ /
*.py[cod]
* $py.


class

# C extensions
*.so

# Distribution / packaging
.Python
build /
develop - eggs /
dist /
downloads /
eggs /
.eggs /
lib /
lib64 /
parts /
sdist /
var /
wheels /
*.egg - info /
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip - log.txt
pip - delete - this - directory.txt

# Unit test / coverage reports
htmlcov /
.tox /
.nox /
.coverage
.coverage. *
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis /
.pytest_cache /

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance /
.webassets - cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs / _build /

# PyBuilder
target /

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default /
ipython_config.py

# pyenv
.python - version

# celery beat schedule file
celerybeat - schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env /
venv /
ENV /
env.bak /
venv.bak /

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/ site

# mypy
.mypy_cache /
.dmypy.json
dmypy.json

# WRD specific
.wrd /
wrd.log
*.wrd.bak

---

# LICENSE
MIT
License

Copyright(c)
2025
WRD(Word)
Contributors

Permission is hereby
granted, free
of
charge, to
any
person
obtaining
a
copy
of
this
software and associated
documentation
files(the
"Software"), to
deal
in the
Software
without
restriction, including
without
limitation
the
rights
to
use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies
of
the
Software, and to
permit
persons
to
whom
the
Software is
furnished
to
do
so, subject
to
the
following
conditions:

The
above
copyright
notice and this
permission
notice
shall
be
included in all
copies or substantial
portions
of
the
Software.

THE
SOFTWARE
IS
PROVIDED
"AS IS", WITHOUT
WARRANTY
OF
ANY
KIND, EXPRESS
OR
IMPLIED, INCLUDING
BUT
NOT
LIMITED
TO
THE
WARRANTIES
OF
MERCHANTABILITY,
FITNESS
FOR
A
PARTICULAR
PURPOSE
AND
NONINFRINGEMENT.IN
NO
EVENT
SHALL
THE
AUTHORS
OR
COPYRIGHT
HOLDERS
BE
LIABLE
FOR
ANY
CLAIM, DAMAGES
OR
OTHER
LIABILITY, WHETHER
IN
AN
ACTION
OF
CONTRACT, TORT
OR
OTHERWISE, ARISING
FROM,
OUT
OF
OR
IN
CONNECTION
WITH
THE
SOFTWARE
OR
THE
USE
OR
OTHER
DEALINGS
IN
THE
SOFTWARE.

---

# README.md
# WRD (Word) - Narzędzie Workflow dla Claude Code

![Python](https: // img.shields.io / badge / python - 3.8 + -blue.svg)
![License](https: // img.shields.io / badge / license - MIT - green.svg)
![Platform](https: // img.shields.io / badge / platform - Fedora - blue.svg)

WRD(Word)
to
zaawansowane
narzędzie
workflow
stworzone
z
myślą
o
efektywnej
pracy
z
Claude
Code
na
systemie
Fedora
Linux.Inspirowane
realnym
doświadczeniem
użytkownika, który
przez
3
tygodnie
intensywnie
wykorzystywał
Claude
Code
do
realizacji
projektów.

## 🚀 Główne funkcjonalności

- ** Zarządzanie
projektami ** - Automatyczne
tworzenie
struktury
projektów
z
szablonami
- ** Integracja
z
Claude
Code ** - Optymalizacja
workflow
pod
kątem
5 - godzinnych
sesji
- ** Automatyczna
dokumentacja ** - Generowanie
plików
CLAUDE.md
i
śledzenie
postępu
- ** Multi - tool
workflow ** - Wsparcie
dla
Claude
Code, Gemini
CLI, Cursor
- ** Smart
commits ** - Automatyczne
opisy
commitów
i
dokumentacja
zmian
- ** Backup & archiwizacja ** - Bezpieczne
przechowywanie
projektów

## 💻 Wymagania systemowe

- ** OS **: Fedora
Linux(testowane
na
najnowszych
wersjach)
- ** Python **: 3.8 +
- ** Git **: dla
zarządzania
wersjami
- ** Claude
Code **: dostęp
do
narzędzia(wymaga
subskrypcji
Claude
Pro)

## 📦 Instalacja

### Szybka instalacja na Fedorze

```bash
# Klonowanie repozytorium
git
clone
https: // github.com / username / wrd.git
cd
wrd

# Konfiguracja środowiska
make
setup - fedora

# Aktywacja środowiska
source
~ /.wrd - env / bin / activate

# Instalacja w trybie deweloperskim
make
install - dev
```

### Instalacja z PyPI (gdy dostępne)

```bash
pip
install
wrd
```

### Instalacja manualna

```bash
# Tworzenie środowiska wirtualnego
python3 - m
venv
~ /.wrd - env
source
~ /.wrd - env / bin / activate

# Instalacja zależności
pip
install - r
requirements.txt

# Instalacja w trybie edytowalnym
pip
install - e.
```

## 🛠️ Pierwszy start

```bash
# Sprawdzenie statusu
wrd
status

# Utworzenie pierwszego projektu
wrd
create
moj - pierwszy - projekt - -type
python - -description
"Testowy projekt WRD"

# Lista projektów
wrd
list

# Przejście do workspace
cd
~ / claude - projects / moj - pierwszy - projekt
```

## 📖 Podstawowe użycie

### Tworzenie projektów

```bash
# Projekt Python
wrd
create
api - serwer - -type
python - -description
"REST API z FastAPI"

# Projekt data science
wrd
create
analiza - danych - -type
data - -description
"Analiza danych sprzedażowych"

# Projekt web
wrd
create
dashboard - -type
fastapi - -description
"Dashboard administratora"
```

### Zarządzanie postępem

```bash
# Aktualizacja postępu
wrd
progress
moj - projekt
"Implementacja logiki biznesowej"

# Automatyczny commit
wrd
commit
moj - projekt - -message
"Dodanie modułu uwierzytelniania"

# Backup wszystkich projektów
wrd
backup
```

### Workflow z Claude Code

1. ** Planowanie ** (Gemini 2.5 Pro / Claude.ai):
```bash
# Utwórz specyfikację w Claude.ai
# Zapisz do pliku CLAUDE.md w projekcie
```

2. ** Implementacja ** (Claude Code):
```bash
# Aktywuj środowisko projektu
cd
~ / claude - projects / nazwa - projektu
source
venv / bin / activate

# Rozpocznij sesję Claude Code (5h)
claude - code
dev
```

3. ** Dokumentacja ** (WRD):
```bash
# WRD automatycznie śledzi postęp
wrd
progress
nazwa - projektu
"Ukończenie modułu X"
```

## 🏗️ Struktura projektu

Każdy
projekt
tworzony
przez
WRD
ma
następującą
strukturę:

```
projekt /
├── src /  # Kod źródłowy
├── tests /  # Testy jednostkowe
├── docs /  # Dokumentacja
├── scripts /  # Skrypty pomocnicze
├── config /  # Pliki konfiguracyjne
├── venv /  # Środowisko wirtualne Python
├── README.md  # Podstawowa dokumentacja
├── CLAUDE.md  # Dokumentacja dla Claude Code
├── requirements.txt  # Zależności Python
└──.gitignore  # Git ignore
```

## ⚙️ Konfiguracja

WRD
przechowuje
konfigurację
w
`~ /.wrd / config.json
`:

```json
{
    "ai_tools": {
        "claude_code": {"enabled": true, "priority": 1},
        "gemini_cli": {"enabled": false, "priority": 2},
        "cursor": {"enabled": false, "priority": 3}
    },
    "workflows": {
        "documentation_auto": true,
        "commit_auto_describe": true,
        "project_templates": true
    },
    "limits": {
        "session_duration": 5,
        "max_concurrent_projects": 3
    }
}
```

## 🔧 Rozwój

### Przygotowanie środowiska deweloperskiego

```bash
# Instalacja zależności deweloperskich
make
install - dev

# Formatowanie kodu
make
format

# Analiza kodu
make
lint

# Uruchomienie testów
make
test

# Budowanie pakietu
make
build
```

### Testowanie

```bash
# Wszystkie testy
pytest

# Testy z pokryciem
pytest - -cov = wrd

# Testy konkretnego modułu
pytest
tests / test_manager.py
```

## 📊 Przykłady użycia

### Ekspresowy projekt w 48h (konkurs)

```bash
# Dzień 1: Setup i architektura (2h)
wrd
create
konkurs - app - -type
fastapi - -description
"Aplikacja konkursowa"
cd
~ / claude - projects / konkurs - app

# Planowanie w Claude.ai → specyfikacja w CLAUDE.md
# Sesja Claude Code #1 (5h): podstawowa struktura

# Dzień 2: Implementacja (8h)
# Sesja Claude Code #2 (5h): główna funkcjonalność
# Sesja Claude Code #3 (3h): finalizacja i deploy

wrd
progress
konkurs - app
"Aplikacja gotowa do zgłoszenia"
wrd
backup  # Zabezpieczenie przed deadlinem
```

### Długoterminowy projekt narzędziowy

```bash
# Setup projektu
wrd
create
moje - narzedzie - -type
python - -description
"Autorskie narzędzie CLI"

# Iteracyjny rozwój
# Tydzień 1: MVP
wrd
progress
moje - narzedzie
"MVP - podstawowe funkcje"

# Tydzień 2: Rozszerzenia
wrd
progress
moje - narzedzie
"Dodanie funkcji zaawansowanych"

# Tydzień 3: Optimalizacje
wrd
progress
moje - narzedzie
"Optymalizacja wydajności"
```

## 🐛 Znane problemy i rozwiązania

### Problem: Limity Claude Code (reset co 5h)
** Rozwiązanie **: WRD
automatycznie
śledzi
czas
sesji
i
przypomina
o
limitach

### Problem: Dokumentacja się rozjeżdża
** Rozwiązanie **: Automatyczne
aktualizacje
CLAUDE.md
przy
każdym
commicie

### Problem: Zgubienie kontekstu między sesjami
** Rozwiązanie **: Szczegółowa
dokumentacja
postępu
w
plikach.md

## 🤝 Współpraca

Chętnie
przyjmujemy
pull
requesty! Zobacz[CONTRIBUTING.md](CONTRIBUTING.md)
aby
dowiedzieć
się
więcej.

1.
Fork
repozytorium
2.
Utwórz
branch
funkcjonalności(`git
checkout - b
feature / AmazingFeature
`)
3.
Commit
zmian(`git
commit - m
'Add some AmazingFeature'
`)
4.
Push
do
brancha(`git
push
origin
feature / AmazingFeature
`)
5.
Otwórz
Pull
Request

## 📝 Changelog

### v1.0.0 (2025-06-28)
- ✨ Pierwsza
wersja
WRD
- 🚀 Podstawowe
zarządzanie
projektami
- 📖 Automatyczna
dokumentacja
CLAUDE.md
- 🔧 Integracja
z
Claude
Code
workflow
- 💾 System
backupów
- 🐧 Optymalizacja
dla
Fedora
Linux

## 📄 Licencja

Projekt
jest
dostępny
na
licencji
MIT.Zobacz[LICENSE](LICENSE)
aby
uzyskać
więcej
informacji.

## 🙏 Podziękowania

- ** Claude
Code
Team ** - za
genialny
tool
CLI
- ** Anthropic ** - za
Claude
AI
- ** Społeczność
Fedora ** - za
stabilny
system
- ** Wszyscy
testerzy ** - za
feedback
i
sugestie

---

*WRD(Word) - Gdy
słowa
zamieniają
się
w
kod * 🚀