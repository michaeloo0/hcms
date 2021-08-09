FROM python:3.9

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
RUN apt-get install git

CMD ["gunicorn", "healthcare_information_system:wsgi:application", "--bind" "0.0.0.0:8000"]