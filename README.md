# djangotemplate
## Setup
### Install pyenv
#### Link for pyenv
```
https://github.com/pyenv/pyenv
```
#### Install python 3.12 version
```bash
pyenv install 3.12
```
### Install poetry
#### Link for poetry
```
https://python-poetry.org/docs/#installation
```
### Create project with poetry
```bash
git clone git@github.com:alukardv/djangotemplate.git
cd ltgh3
```
#### Create virtual environments
```bash
pyenv local 3.12
```
#### Install requirements
```bash
poetry install
```
#### Create .env
```bash
cp .env.example .env
```

#### edit .env
```bash
vi .env
```
## DB migrate
### with poetry
```bash
poetry run python manage.py migrate
```
## Createsuperuser
```bash
poetry run python manage.py createsuperuser
```
