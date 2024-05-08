FROM python:3-bullseye

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 80
ENTRYPOINT ["gunicorn",  "-b", ":80", "app:app"]
