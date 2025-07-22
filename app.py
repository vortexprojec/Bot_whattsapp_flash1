from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get("Body").lower().strip()
    resp = MessagingResponse()
    msg_resp = resp.message()

    if msg == "hola":
        msg_resp.body("👋 ¡Hola! Soy tu asistente. Escribe:\n1️⃣ Ver menú\n2️⃣ Hacer pedido\n3️⃣ Hablar con alguien")
    elif msg == "1":
        msg_resp.body("🍽️ Menú del día:\n- Pollo\n- Arroz\n- Agua de jamaica")
    elif msg == "2":
        msg_resp.body("📝 Envíame tu pedido con:\nPlatillo:\nDirección:\nTeléfono:")
    else:
        msg_resp.body("❓ No entendí. Escribe *hola* para ver el menú.")

    return str(resp)

if __name__ == "__main__":
    app.run()
