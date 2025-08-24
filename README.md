# API de Análisis de Sentimientos con FastAPI y Transformers 🤖

Este proyecto expone un modelo de análisis de sentimientos de Hugging Face mediante una API construida con **FastAPI**.  

---

## 📦 Requisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Postman (para pruebas, opcional)

---

## ⚙️ Instalación de dependencias

Clona este repositorio y dentro de la carpeta del proyecto instala las dependencias:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener, al menos:

```
fastapi
pydantic
transformers
torch
uvicorn
```

---

## 🚀 Ejecutar el servidor

Para levantar el servidor en modo desarrollo ejecuta:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en:

```
http://127.0.0.1:8000
```

---

## 📖 Documentación automática

FastAPI genera documentación interactiva automáticamente:

- **Swagger UI**:  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

- **Redoc**:  
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔍 Endpoints disponibles

### 1. GET `/`
Verifica que la API esté funcionando.

**Ejemplo en Postman**
1. Abre Postman.
2. Crea una nueva petición.
3. Selecciona método **GET**.
4. En la URL escribe:
   ```
   http://127.0.0.1:8000/
   ```
5. Haz clic en **Send**.

**Respuesta esperada:**
```json
{
  "message": "API de mi modelo funcionando 🚀"
}
```

---

### 2. POST `/predict`
Realiza un análisis de sentimiento sobre un texto enviado.

**Ejemplo en Postman**
1. Abre Postman.
2. Crea una nueva petición.
3. Selecciona método **POST**.
4. En la URL escribe:
   ```
   http://127.0.0.1:8000/predict
   ```
5. Ve a la pestaña **Headers** y agrega:
   ```
   Key: Content-Type
   Value: application/json
   ```
6. Ve a la pestaña **Body** → selecciona **raw** → elige **JSON**.
7. Escribe el siguiente JSON de ejemplo:
   ```json
   {
     "text": "Me encanta esta moto"
   }
   ```
8. Haz clic en **Send**.

**Respuesta esperada:**
```json
{
  "result": [
    {
      "label": "POSITIVE",
      "score": 0.9993
    }
  ]
}
```

---

## 🐍 Ejemplo en Python (opcional)

También puedes probar el endpoint desde un script Python con `requests`:

```python
import requests

url = "http://127.0.0.1:8000/predict"
data = {"text": "Me encanta esta moto 🚀"}

response = requests.post(url, json=data)
print(response.json())
```

---

## 🛠 Tecnologías usadas

- [FastAPI](https://fastapi.tiangolo.com/) - Framework para la API
- [Transformers](https://huggingface.co/transformers/) - Modelos de NLP
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI
- [Pydantic](https://docs.pydantic.dev/) - Validación de datos
