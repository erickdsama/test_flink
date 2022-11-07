FROM python:3.10

WORKDIR /testFlink

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /testFlink/
RUN pip install -r requirements.txt

COPY . /testFlink

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

