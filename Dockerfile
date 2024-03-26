FROM python:3.12-slim 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

