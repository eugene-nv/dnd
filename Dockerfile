FROM python:3.11

WORKDIR /project

COPY . /project

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]