FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

RUN mkdir /code
RUN apt update -y
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
