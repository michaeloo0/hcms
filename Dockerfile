FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000
RUN apt-get install git

CMD ["gunicorn", "healthcare_information_system:wsgi:application", "-c", "./gunicorn.conf.py"]