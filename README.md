# **ViaAppia**
## **Descrição**
O **ViaAppia** é uma API intermediária entre os sistemas da NUTEC e o SuperSapiens. Ele fornece rotas puras para acesso direto às informações do SuperSapiens e rotas específicas que estruturam os dados conforme as necessidades dos sistemas consumidores.

A API foi projetada para garantir uma comunicação eficiente, padronizada e segura entre os sistemas, facilitando a integração com múltiplas tecnologias.

---

## **Tecnologias Utilizadas**
- **Python** com **FastAPI** (Backend)
- **Pydantic** (Validação de dados)
- **Requests** (Requisições HTTP)
- **Uvicorn** (Servidor ASGI)
- **Supersapiens API** (Fonte de dados principal)

---

## **Instalação**
### **1️. Clone o repositório**
```bash
git clone https://github.com/Pace-pfpa/via-appia
```

### **2. Instale as dependências**
Caso esteja rodando localmente:
``` sh
pip install -r requirements.txt
```

### **3. Configuração**
Copie o arquivo .env-example e renomeie para .env, e preencha as variáveis de ambiente com as configurações necessárias.:
``` sh
cp .env-example .env
```

## **Rodando o Projeto**
### **Com Python diretamente**
```sh
fastapi run
```

## **Endpoints**
A documentação completa dos endpoints está disponível via Swagger após iniciar o servidor:
- Swagger UI
- Redoc
---

## **Contribuições**
Atualmente, a contribuição é restrita a membros da equipe "viappia" na organização Nutec-PFPA no GitHub.

Seu Afonso é daora.
