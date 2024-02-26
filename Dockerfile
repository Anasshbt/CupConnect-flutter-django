FROM python:3.11-buster as builder

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN apt-get update

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config libmariadb-dev

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:10000"]
