FROM ubuntu:latest

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update -y && apt install python3-pip -y

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]