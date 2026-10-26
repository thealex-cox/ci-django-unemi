# Imagen base solicitada por la guía
FROM python:3.10-slim

# Evita archivos .pyc y muestra los logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalación de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia del código del proyecto
COPY . .

# Script de arranque (se eliminan saltos de línea de Windows)
RUN sed -i 's/\r$//' entrypoint.sh && chmod +x entrypoint.sh

# Puerto donde corre Django
EXPOSE 8000

# Configuración de ENTRYPOINT
ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]