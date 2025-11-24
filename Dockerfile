# Dockerfile para Capusotto API
# Usa Gunicorn con workers Uvicorn para servir la aplicación ASGI en producción

FROM python:3.13.3-slim

# Crear un usuario no-root por seguridad
RUN useradd --create-home appuser

WORKDIR /app

# Evitar que Python escriba .pyc y activar flush de stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar dependencias del sistema necesarias para compilar paquetes
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias (capa cacheable)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn

# Copiar el código de la aplicación
COPY . /app

# Asegurar que exista la carpeta de datos y asignar permisos
RUN mkdir -p /app/data && chown -R appuser:appuser /app

USER appuser

# Puerto expuesto por el contenedor
EXPOSE 8000

# Comando por defecto: Gunicorn con Uvicorn worker (ajusta -w según CPU)
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "-b", "0.0.0.0:8000", "main:app"]
