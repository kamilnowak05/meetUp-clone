FROM python:3.11-buster

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:/app/"

COPY ./requirements.txt /app/

WORKDIR /app

RUN apt-get update && apt-get install gettext -y

RUN pip install -U pip==23.0 && pip install -r requirements.txt

COPY ./app /app
COPY ./.env /app/.env

CMD python /backend/manage.py collectstatic --noinput
