# Bot de WhatsApp con FastAPI y Evolution API

Este proyecto es un microservicio que permite recibir y responder mensajes de WhatsApp automáticamente usando Evolution API y FastAPI. Ideal para integraciones de chatbots y atención automatizada.

## Requisitos

- Python 3.8+
- Docker (para Evolution API)
- Cuenta y servicio Evolution API funcionando
- (Opcional) Cuenta en Render.com para despliegue en la nube

## Instalación local

1. Clona este repositorio o copia los archivos en una carpeta nueva:

```bash
cd wpp-bot-fastapi
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Configura las variables de entorno (puedes usar un archivo `.env` o configurarlas en tu entorno):

- `EVOLUTION_API_URL` — URL de tu instancia Evolution API (ej: `http://localhost:8080`)
- `EVOLUTION_API_KEY` — Tu clave secreta definida en Evolution API
- `INSTANCE_NAME` — Nombre de la instancia de WhatsApp creada en Evolution API

3. Ejecuta el bot localmente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 10000
```

El endpoint del webhook estará disponible en: `http://localhost:10000/webhook`

---

## Despliegue en Render

1. Sube este proyecto a un repositorio de GitHub.
2. Entra a [https://dashboard.render.com/](https://dashboard.render.com/) y crea un nuevo servicio web.
3. Selecciona tu repo y configura:
   - **Start command:**
     ```
     uvicorn main:app --host 0.0.0.0 --port 10000
     ```
   - **Variables de entorno:**
     - `EVOLUTION_API_URL`
     - `EVOLUTION_API_KEY`
     - `INSTANCE_NAME`

4. Render te dará una URL pública, por ejemplo:
   `https://tu-bot-en-render.onrender.com/webhook`

---

## Configuración de Evolution API

1. Instala y ejecuta Evolution API siguiendo la [documentación oficial](https://doc.evolution-api.com/v1/pt/install/docker).
2. Crea una instancia de WhatsApp y conecta tu número escaneando el QR.
3. Configura el webhook de Evolution API para que apunte a la URL de tu bot:
   - Ejemplo: `https://tu-bot-en-render.onrender.com/webhook`

---

## ¿Cómo funciona?

- Cuando un usuario envía un mensaje de WhatsApp, Evolution API lo reenvía a `/webhook`.
- El bot procesa el mensaje y responde automáticamente usando Evolution API.
- Puedes personalizar la lógica de respuesta en el archivo `main.py`.

---

## Personalización

Edita la función `webhook` en `main.py` para cambiar la lógica de respuesta automática.

---

## Licencia

MIT 