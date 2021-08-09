FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000
RUN apt-get install git
RUN python migrate 
RUN python makemigrations

CMD ["python", "manage.py", "runserver" "0.0.0.0:8000"]