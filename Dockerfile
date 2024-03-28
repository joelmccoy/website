FROM python:3.12-slim 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . app
WORKDIR /app

EXPOSE 8000

RUN python manage.py collectstatic --noinput

# CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 mysite.wsgi:application

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
