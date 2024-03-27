refresh-reqs:
	uv pip compile requirements.in -o requirements.txt

install-reqs:
	uv pip install -r requirements.txt
	uv pip install -r dev-requirements.txt

docker-build:
	docker build -t website:latest .

docker-run: docker-build
	docker run -p 8000:8000 website:latest

db-up:
	docker-compose up -d

db-down:
	docker-compose down

migrations: db-up
	python manage.py makemigrations
	python manage.py migrate

create-admin:
	python manage.py createsuperuser

bootstrap-db:
	python manage.py runscript bootstrap_things

run:
	python manage.py runserver
