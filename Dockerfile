FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc netcat
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

RUN mkdir /app -p && mkdir /app/static -p
WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]