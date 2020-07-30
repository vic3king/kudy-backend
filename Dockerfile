FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/

ARG APP_SETTINGS

ENV APP_SETTINGS=${APP_SETTINGS} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  POETRY_VERSION=1.0.0

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$APP_SETTINGS" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /code
ENV PYTHONPATH=/code
