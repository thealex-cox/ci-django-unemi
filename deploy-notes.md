# Notas de despliegue simulado – ci-django-unemi

Proyecto: Flujo CI/CD para Django
Asignatura: Gestión de la Configuración de Software – UNEMI
Responsable de la Sesión 3: German Steven Riera Rebolledo

## 1. Objetivo

Simular el despliegue del sistema en una carpeta externa al entorno de desarrollo, como si fuera un servidor de producción, usando únicamente Git y Docker.

## 2. Requisitos del equipo de destino

- Git instalado
- Docker Desktop en ejecución (Docker Engine y Docker Compose)
- Puerto 8000 libre

No se requiere instalar Python ni PostgreSQL: ambos se ejecutan dentro de los contenedores.

## 3. Despliegue automatizado (GitHub Actions)

El archivo `.github/workflows/ci.yml` tiene dos jobs:

1. **test**: instala dependencias y ejecuta las pruebas contra PostgreSQL.
2. **build-deploy** (depende de `test`):
   - Construye la imagen Docker `ci-django-unemi`.
   - La etiqueta para DockerHub (push simulado).
   - Exporta la imagen como `ci-django-unemi-image.tar.gz` y la guarda como artefacto en GitHub.
   - Levanta el sistema con Docker Compose y valida con `curl` que `/tareas/` responde.
   - Muestra los registros y elimina los contenedores.

## 4. Despliegue manual simulado en carpeta externa

### 4.1 Crear la carpeta de despliegue y descargar el proyecto

```bash
mkdir C:\despliegue-simulado
cd C:\despliegue-simulado
git clone -b cd-setup https://github.com/thealex-cox/ci-django-unemi.git produccion
cd produccion
```

### 4.2 Ejecutar con Docker Compose

```bash
docker compose up -d --build
docker compose ps
docker compose logs web
```

### 4.3 Validar desde el navegador

Abrir: http://localhost:8000/tareas/

Respuesta esperada:

```json
{"total": 0, "tareas": []}
```

### 4.4 Detener el despliegue

```bash
docker compose down
```

## 5. Alternativa: desplegar desde el artefacto de GitHub

1. En GitHub, ir a **Actions**, abrir la última ejecución exitosa y descargar el artefacto `ci-django-unemi-image`.
2. Descomprimir el `.zip` en la carpeta de despliegue.
3. Cargar la imagen:

```bash
docker load -i ci-django-unemi-image.tar.gz
docker images ci-django-unemi
```

4. Con el `docker-compose.yml` en la misma carpeta, levantar sin reconstruir:

```bash
docker compose up -d --no-build
```

## 6. Problemas frecuentes

| Problema | Solución |
|---|---|
| `port is already allocated` | Detener otros contenedores que usen el puerto 8000 con `docker compose down` |
| `entrypoint.sh: not found` | Verificar saltos de línea LF; el Dockerfile ya los corrige con `sed` |
| La página no carga de inmediato | Esperar unos segundos a que se apliquen las migraciones |