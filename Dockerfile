# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu aplicación al directorio de trabajo
COPY . /app

# Instala las dependencias de tu aplicación
RUN test -e requirements.txt && pip install --no-cache-dir -r requirements.txt || true

# Define el comando por defecto para ejecutar tu aplicación cuando se inicie el contenedor
CMD ["python", "main.py"]
