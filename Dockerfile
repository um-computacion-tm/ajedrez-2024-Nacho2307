FROM python:3-alpine

RUN apk add --no-cache git redis

RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-Nacho2307.git

WORKDIR /ajedrez-2024-Nacho2307

RUN pip install -r requirements.txt

# Iniciar Redis en segundo plano y luego ejecutar tu aplicación
CMD ["sh", "-c", "redis-server --daemonize yes && coverage run -m unittest && coverage report -m && python main.py"]

# docker buildx build -t ajedrez-2024-nacho2307.
# docker run -i ajedrez-2024-nacho2307