.PHONY: install
install:
	poetry install

.PHONY: runserver
runserver:
	poetry run python manage.py runserver

.PHONY: createsuperuser
createsuperuser:
	poetry run python manage.py createsuperuser

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: createapp
createapp:
	poetry run python manage.py startapp 

.PHONY: update
update: install migrate ;
