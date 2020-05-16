# Notes Web

Notes Application - Web implementation

## Setup

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -U -r requirements.dev.txt
```

## Run dev

```bash
$ python server.py
```

or 

```bash
$ source .venv\bin\activate
$ export FLASK_APP=notes
$ export FLASK_ENV=development
$ flask run
```

or Windows PowerShell

```
> & .venv\Scripts\Activate.ps1
> $env:FLASK_ENV = "development"
> $env:FLASK_APP = "notes"
> flask run
```

or Windows CMD

```shell
> .venv\Scripts\activate.bat
> set FLASK_ENV=development
> set FLASK_APP=notes
> flask run
```
