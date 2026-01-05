import os
import logging
from flask import Flask, render_template, request

# Configuração de logs
logging.basicConfig(level=logging.INFO)

# Carrega variáveis do .env
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Função simulada de envio de WhatsApp (não envia realmente)
def enviar_whatsapp(nome, telefone, servico, mensagem):
    try:
        instance = os.getenv("ZAPI_INSTANCE", "YOUR_INSTANCE_ID")
        token = os.getenv("ZAPI_TOKEN", "YOUR_CLIENT_TOKEN")
        destino = os.getenv("DESTINO_WHATSAPP", "YOUR_PHONE_NUMBER")

        # Aqui apenas simula envio
        texto = (
            f"📌 Novo pedido de orçamento\n\n"
            f"👤 Nome: {nome}\n"
            f"📞 Telefone: {telefone}\n"
            f"🛠 Serviço: {servico}\n"
            f"📝 Mensagem: {mensagem}\n\n"
            f"(Simulação: instância={instance}, token={token}, destino={destino})"
        )

        logging.info("Mensagem simulada enviada:")
        logging.info(texto)

        # Retorna sucesso simulado
        return True

    except Exception as e:
        logging.error(f"Erro simulado: {e}")
        raise

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        servico = request.form.get("servico")
        mensagem = request.form.get("mensagem")

        try:
            enviar_whatsapp(nome, telefone, servico, mensagem)
            return render_template("index.html", sucesso=True)
        except Exception as e:
            return render_template("index.html", erro=True, mensagem=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
