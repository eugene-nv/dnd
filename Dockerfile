FROM python:3.11

COPY . /project

ENTRYPOINT ['python', 'manage.py']

CMD ['runserver', '0.0.0.0:8000']