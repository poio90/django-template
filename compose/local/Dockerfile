FROM python:3.11.9-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema necesarias
RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev gettext

# install dependencies
RUN pip install --upgrade pip

# Copiar los archivos de requerimientos e instalarlos
COPY ./compose/requirements /requirements
RUN pip install --no-cache-dir -r /requirements/local.txt

# Copiar el resto de la aplicación
COPY ./app/ .

# Exponer el puerto en el que correrá el servicio
EXPOSE 8000

# Comando por defecto para ejecutar el servidor
# CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]