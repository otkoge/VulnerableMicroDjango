FROM python:3.8-alpine
RUN  apk update && apk add --no-cache docker net-tools
RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/
ADD containAdmin /opt/app/containAdmin
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
EXPOSE 8000
CMD ["python", "/opt/app/containAdmin/manage.py", "runserver", "0.0.0.0:8000"]
