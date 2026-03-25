# segundaParteParcialEntornoDeDesarrollo

## Descripción

API básica con FastAPI que usa Google GenAI (Gemini) para generar texto a partir de un prompt.

## Dependencias

- Python 3.10+
- fastapi
- uvicorn
- python-dotenv
- google-genai

Instalación:

```bash
pip install fastapi uvicorn python-dotenv google-genai
```

## Configuración

1. Crea un archivo `.env` en la raíz:

```env
GEMINI_API_KEY=tu_api_key_aqui
```

2. Agrega `.gitignore` para evitar subir la clave:

```
.env
.venv/
__pycache__/
```

## main.py

Código recomendado:

```python
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Falta GEMINI_API_KEY en el entorno")

client = genai.Client(api_key=api_key)
app = FastAPI()

@app.get("/llm/{prompt}")
async def read_root(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return {"Respuesta": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Uso

1. Ejecuta el servidor:

```bash
uvicorn main:app --reload
```

2. Prueba el endpoint:

```bash
curl "http://127.0.0.1:8000/llm/Hola"
```

3. Respuesta esperada:

```json
{"Respuesta": "Texto generado por Gemini..."}
```

## Solución de errores

- `401 Unauthorized`: clave inválida o sin permisos.
- `RuntimeError("Falta GEMINI_API_KEY en el entorno")`: revisa el archivo `.env` y la variable `GEMINI_API_KEY`.
- Si el entorno es Docker/CI, exporta la clave en la variable de entorno correspondiente.

## Seguridad

- Nunca subir `.env` con la API KEY.
- Regenera la clave si se filtra.

## Avance

- Añade validación de longitud de prompt, logs de uso y rate limiting si quieres escalar.
