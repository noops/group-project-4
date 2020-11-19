FROM ubuntu:latest

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip \
    libpq-dev

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]