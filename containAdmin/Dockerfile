FROM python:3.8-alpine
RUN  apk update && apk add --no-cache docker net-tools postgresql-dev gcc python3-dev musl-dev
RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/
ADD . /opt/app/containAdmin
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait
CMD ["/opt/app/containAdmin/manage.py", "runserver", "0.0.0.0:8000"]
