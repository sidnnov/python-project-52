LOCAL := poetry run python manage.py

install:
	poetry install

uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 task_manager

test-coverage:
	poetry run coverage run manage.py test

messages:
	poetry run django-admin makemessages -l ru

compilemess:
	poetry run django-admin compilemessages

server:
	$(LOCAL) runserver

migrations:
	$(LOCAL) makemigrations

migrate:
	$(LOCAL) migrate
