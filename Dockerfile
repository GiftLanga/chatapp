FROM python:3.6

RUN mkdir -p /opt/services/chatApp
WORKDIR /opt/services/chatApp

COPY . /opt/services/chatApp

RUN pip install -r ./requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--chdir", "chatApp", "--bind", ":8000", "chatApp.wsgi:application"]