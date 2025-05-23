# VirusTotal File Scan API

## Ing. Florentino Ramirez Balderas

## Descripción
API construida con FastAPI que permite subir archivos, escanearlos con VirusTotal y devolver los resultados.

## Ejecutar con Docker

### Requisitos
- Docker
- API Key de VirusTotal

### Instrucciones

# Crear el archivo .env
echo "VIRUSTOTAL_API_KEY=API" > .env

# Construir la imagen
docker build -t virustotal-api .

# Correr el contenedor
docker run -p 8000:8000 --env-file .env virustotal-api
