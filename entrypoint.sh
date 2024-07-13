#!/bin/bash

echo "${POSTGRES_USER}"

postgres_ready() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_NAME}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
  >&2 echo "Waiting for PostgreSQL to become available..."
  sleep 1
done
>&2 echo "PostgreSQL is available"

python manage.py migrate --no-input

python manage.py collectstatic --no-input

gunicorn high_hill.wsgi:application --bind 0.0.0.0:8000

exec "$@"