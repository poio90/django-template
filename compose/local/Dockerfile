FROM python:3.11.9-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema necesarias
RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev

# Copiar los archivos de requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto en el que correrá el servicio
EXPOSE 8000

# Comando por defecto para ejecutar el servidor
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]