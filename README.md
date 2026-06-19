# Todo API
API REST desarrollada en Python utilizando FastAPI para gestionar una lista de tareas.

## Requisitos
- Python 3.11+
- Docker

## Instalación local
Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/todo-api.git
cd todo-api
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

### Windows
```bash
venv\Scripts\activate
```

### Linux/Mac
```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
uvicorn main:app --reload
```

La API estará disponible en:

```
http://localhost:8000
```

Documentación interactiva:

```
http://localhost:8000/docs
```

---

## Ejecución con Docker

Construir la imagen:

```bash
docker build -t todo-api .
```

Ejecutar el contenedor:

```bash
docker run -p 8000:8000 todo-api
```

La API estará disponible en:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## Endpoints disponibles

| Método | Endpoint | Descripción |
|----------|----------|----------|
| GET | /tasks | Obtener todas las tareas |
| POST | /tasks | Crear una tarea |
| PUT | /tasks/{id} | Actualizar una tarea |
| DELETE | /tasks/{id} | Eliminar una tarea |

## Ejemplo de creación de tarea

### POST /tasks

Body:

```json
{
  "title": "Aprender FastAPI"
}
```

Respuesta:

```json
{
  "id": 1,
  "title": "Aprender FastAPI",
  "completed": false
}
```