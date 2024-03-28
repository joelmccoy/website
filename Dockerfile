FROM python:3.12-slim 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . app
WORKDIR /app

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD ["sh", "-c", "gunicorn website.wsgi:application --bind :$PORT"]

