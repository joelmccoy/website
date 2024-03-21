refresh-reqs:
	uv pip-compile requirements.in -o requirements.txt

install-reqs:
	uv pip install requirements.txt

run:
	python manage.py runserver
