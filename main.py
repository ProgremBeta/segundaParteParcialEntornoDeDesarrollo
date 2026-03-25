from fastapi import FastAPI 
from dotenv import load_dotenv 
from google import genai 

app = FastAPI() 
KEY = load_dotenv("APY_KEY") 

@app.get("/llm/{prompt}") 

async def read_root(prompt): 

# The client gets the API key from the environment variable `GEMINI_API_KEY`. client = genai.Client() 
response = client.models.generate_content( 
model="gemini-3-flash-preview", contents=prompt 
) 
print(response.text) 
return {"Respuesta": response.text} 
