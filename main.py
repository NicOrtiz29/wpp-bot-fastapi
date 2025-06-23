from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx
import os

app = FastAPI()

# Configuración desde variables de entorno o valores por defecto
EVOLUTION_API_URL = os.getenv("EVOLUTION_API_URL", "http://localhost:8080")
EVOLUTION_API_KEY = os.getenv("EVOLUTION_API_KEY", "TU_API_KEY")
INSTANCE_NAME = os.getenv("INSTANCE_NAME", "mi-primer-chatbot")
CLIENTES_DIR = os.getenv("CLIENTES_DIR", "clientes")  # Carpeta donde están los archivos de clientes

def obtener_respuesta_personalizada(numero):
    # El número debe estar en formato internacional, sin espacios ni signos
    archivo = os.path.join(CLIENTES_DIR, f"{numero}.txt")
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "¡Hola! ¿En qué puedo ayudarte?"

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Mensaje recibido:", data)

    # Extrae el número y el mensaje recibido
    try:
        numero = data["from"]
        mensaje = data["body"]
    except KeyError:
        return JSONResponse(content={"status": "error", "detail": "JSON inválido"}, status_code=400)

    # Busca la respuesta personalizada
    respuesta = obtener_respuesta_personalizada(numero)

    # Envía la respuesta usando Evolution API
    await enviar_mensaje(numero, respuesta)

    return JSONResponse(content={"status": "ok"})

async def enviar_mensaje(numero, mensaje):
    url = f"{EVOLUTION_API_URL}/message/sendText"
    headers = {"apikey": EVOLUTION_API_KEY}
    payload = {
        "instanceName": INSTANCE_NAME,
        "to": numero,
        "message": mensaje
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(url, json=payload, headers=headers)
        print("Respuesta de Evolution API:", r.text) 