import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("Falta API_KEY en el entorno")

client = genai.Client(api_key=api_key)

app = FastAPI()

@app.get("/llm/{prompt}")
async def read_root(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"Respuesta": response.text}
