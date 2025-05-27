# Bravos Energía – FS Developer Test (Backend)

## Descripción

Este proyecto es parte de la prueba técnica para el puesto de Full Stack Developer en Bravos Energía. Consiste en una aplicación Flask que consume la [Dog API](https://dogapi.dog/docs/api-v2) y expone endpoints estructurados para acceder a información de razas de perros, grupos y datos relacionados.

## Requisitos

- Python 3.8 o superior
- pip (instalador de paquetes de Python)
- Flask

## Instrucciones de uso

### 1. Clona el repositorio

```bash
git clone https://github.com/tlapalep/dogBreed.git
cd dogBreed
```

### 2. Crea y activa un entorno virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # En macOS / Linux
venv\Scripts\activate     # En Windows
```

### 3. Instala Flask

```bash
pip install flask
```

> Nota: Si ves errores relacionados con CORS, puedes instalar también:
> ```bash
> pip install flask-cors
> ```

### 4. Ejecuta el servidor Flask

```bash
python dog_api_backend.py
```

Esto levantará la API en `http://127.0.0.1:5000`.

### 5. Prueba los endpoints

Abre una segunda terminal (con el backend corriendo) y ejecuta:

```bash
python test_endpoints.py
```

Si todo está correcto, verás un resultado con `200 OK` en todos los endpoints y un `# Result: 100.0 %`.

## Endpoints disponibles

- `GET /breeds`
- `GET /breeds/<breed_id>`
- `GET /facts`
- `GET /groups`
- `GET /groups/<group_id>`
- `GET /group-details/<group_id>`
- `GET /group-details/<group_id>/breed/<breed_id>`

Todos los endpoints retornan respuestas JSON válidas, procesadas desde la API externa `https://dogapi.dog/api/v2`.

