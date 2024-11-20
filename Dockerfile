FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /blog-be

WORKDIR /blog-be

ADD . /blog-be/

RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
