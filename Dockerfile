FROM python:3.10-slim-bullseye AS base

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONPATH=/app \
    TZ=America/Sao_Paulo

WORKDIR /app

RUN apt update -y && \
    apt upgrade -y

COPY ./api/ api
COPY ./main.py main.py
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
# ========================= Tests stage
FROM base AS tests

COPY ./tests/ tests
COPY ./requirements_dev.txt requirements_dev.txt
RUN pip install -r requirements_dev.txt
ENTRYPOINT ["python", "pytest"]
# ========================= App stage
FROM base AS app

COPY ./entrypoint.sh entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
