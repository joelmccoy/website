refresh-reqs:
	uv pip compile requirements.in -o requirements.txt

install-reqs:
	uv pip install -r requirements.txt
	uv pip install -r dev-requirements.txt

docker-build:
	docker build -t website:latest .

docker-run: docker-build
	docker run -d -e PORT=8000 -p 8000:8000 website:latest

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
	bash scripts/bootstrap_db.sh

run:
	python manage.py runserver
