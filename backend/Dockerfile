FROM python:3.10.14-bullseye

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 5000
ENTRYPOINT ["gunicorn",  "-b", ":40", "app:app"]
