![Back-end language](https://img.shields.io/badge/python-3.8-yellow)
### ENV
```
Linux:
python3 -m venv  env
source env/bin/activate
Windows :
python -m venv  env
call env/Scripts/activate.bat

```
### Check ENV
```
python -V
```
### How to install requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```
### Create .env 
```
create .env file 
copy .env_example to .env
```
### Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### How to run 
```
python manage.py runserver localhost:3000
```
### Run tests
```
python manage.py test
```
### Go to
```
http://localhost:3000/ddbfa6bdafa18796968244c775cdb6d4/
http://localhost:3000/api/users/
http://localhost:3000/api/users/?page=1
http://localhost:3000/api/users/1

```

### Create Superuser
```
python manage.py createsuperuser
```
