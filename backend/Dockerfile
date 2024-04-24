FROM python:slim-buster

WORKDIR /server

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
