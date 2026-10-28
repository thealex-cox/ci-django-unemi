#!/bin/sh
# Aplica las migraciones antes de iniciar el servidor
python manage.py migrate --noinput
# Ejecuta el comando definido en CMD
exec "$@"