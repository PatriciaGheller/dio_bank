#!/usr/bin/env bash
set -e

poetry run flask --app dio_bank.src.app db upgrade
poetry run gunicorn dio_bank.src.wsgi:app 
