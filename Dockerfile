FROM python:3.12-alpine

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./drf_example_api ./

WORKDIR /drf_example_api

CMD python manage.py runserver

EXPOSE 8000