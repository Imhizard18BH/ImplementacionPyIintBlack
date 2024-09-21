FROM python:3.12

RUN mkdir -p /project/app

COPY ./app /project/app
COPY ./requirements.txt /project

WORKDIR /project

RUN apt-get update && apt-get upgrade -y && apt-get install -y mariadb-client && pip install mysqlclient

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV MYSQL_DATABASE=pylintPep8
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]