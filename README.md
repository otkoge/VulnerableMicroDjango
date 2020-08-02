# VulnerableMicroDjang-
Small example of vulnerable docker setup - DO NOT PUT IN PRODUCTION


docker build -t cadmin:latest .

docker run --name cadmin -p 80:8000 -v /var/run/docker.sock:/var/run/docker.sock:ro cadmin


docker-compose exec web /bin/sh -c "export DJANGO_SUPERUSER_PASSWORD='admin' && python /opt/app/containAdmin/manage.py createsuperuser --noinput --username admin --email admin@admin.local"
