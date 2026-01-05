# WhatsApp Automation - Protótipo

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

## Descrição
Este projeto é um **protótipo de automação de pedidos via WhatsApp**, desenvolvido em Python com Flask.  
Ele simula o envio de mensagens estruturadas a partir de um formulário web.

> ⚠️ Nota: devido a limitações de instâncias de teste da Z-API, o envio real de WhatsApp não está funcional.  
> O foco deste projeto é **demonstrar habilidades em backend, integração de APIs, Flask e tratamento de dados**.



## Funcionalidades

- Formulário web de pedido de orçamento
- Simulação de envio de mensagens WhatsApp
- Logs detalhados de envio
- Tratamento de erros no backend



## Tecnologias Utilizadas

- **Python 3.x** – Backend e lógica
- **Flask** – Servidor web e renderização de formulário
- **Requests** – Preparação de payload para APIs
- **python-dotenv** – Gerenciamento de variáveis de ambiente


## Estrutura do Projeto

whatsapp_automation_portfolio/

├─ app.py # Código principal Flask

├─ templates/
 
   └─ index.html # Formulário web

├─ .env.example # Exemplo de variáveis de ambiente

├─ .gitignore

├─ requirements.txt

└─ README.md
