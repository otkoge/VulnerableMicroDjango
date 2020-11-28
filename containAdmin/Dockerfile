FROM python:3.8-buster
RUN  apt-get update && apt-get install -y net-tools postgresql-server-dev-all gcc python3-dev musl-dev apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce docker-ce-cli
RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/
ADD . /opt/app/containAdmin
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN python /opt/app/containAdmin/manage.py collectstatic --noinput --clear &>/dev/null
RUN chmod +x /wait
CMD ["/opt/app/containAdmin/manage.py", "runserver", "0.0.0.0:8000"]
