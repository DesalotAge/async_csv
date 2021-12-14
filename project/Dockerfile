# pull official base image
FROM python:3.9-alpine

# set environment variables
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0 \
  PYTHONDONTWRITEBYTECODE=1 \ 
  PYTHONUNBUFFERED=1

# deps for poetry
RUN apk add gcc libffi-dev musl-dev postgresql-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

# System deps
RUN pip install --upgrade pip
RUN pip install poetry

# Copy only requirements to cache them in docker layer
WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app

# Project initialization
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Creating folders, and files for a project
COPY . /usr/src/app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]