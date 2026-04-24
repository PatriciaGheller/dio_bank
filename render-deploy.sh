#!/usr/bin/env bash
set -e

pip install poetry
poetry install --no-root

poetry run flask --app dio_bank.src.app db upgrade
poetry run gunicorn dio_bank.src.wsgi:app 
