refresh-reqs:
	uv pip-compile requirements.in -o requirements.txt

install-reqs:
	uv pip install requirements.txt

docker-build:
	docker build -t website:latest .

docker-run: docker-build
	docker run -p 8000:8000 website:latest

run:
	python manage.py runserver
