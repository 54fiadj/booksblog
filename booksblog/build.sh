#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python mywebsite/manage.py collectstatic --no-input
python mywebsite/manage.py migrate