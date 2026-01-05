# WhatsApp Automation - Protótipo

## Descrição
Este projeto é um **protótipo de automação de pedidos via WhatsApp**, desenvolvido em Python com Flask.  
Ele simula o envio de mensagens estruturadas a partir de um formulário web.

> Importante: devido a limitações da Z-API e instâncias de teste, o envio real de WhatsApp não está funcional.  
> O foco deste projeto é demonstrar lógica, backend e integração de APIs.

## Funcionalidades
- Formulário web de pedido de orçamento
- Simulação de envio de mensagem WhatsApp
- Tratamento de erros e logs

## Tecnologias
- Python 3.x
- Flask
- Requests
- python-dotenv

## Como rodar
1. Clone o repositório:
git clone https://github.com/dillanchagas94/whatsapp_automation_portfolio.git
cd whatsapp_automation_portfolio

2.Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale dependências
pip install -r requirements.txt

4.Crie um arquivo .env baseado no .env.exemple

5.Rode o Flask
python app.py

6.Abra no navegador
http://127.0.0.1:5000


## Possiveis evoluções
. Multi-clientes
. Armazenamento de pedidos em JSON ou banco de dados
. Integração com APIs de envio de Whatsapp (Z-API,ChatPro,Cloud API)
. Geração de PDFs automáticos para orçamento
