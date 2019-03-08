# red_string

## CLI to dev:

### Create a virtual Python enviroment:

creates virtual enviroment named venv 
virtualenv --python=python3 venv
source venv/bin/activate

### Install dependences in virtual env:

pip install django==1.11.8 djangorestframework==3.7.3 djangorestframework-jwt==1.11.0


### Migrations:

python3 manage.py makemigrations
python3 manage.py migrate

### Run server:

python3 manage.py runserver

### Create a super user:

python3 manage.py createsuperuser
