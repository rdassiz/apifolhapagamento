# PayFlow

PayFlow é uma API de pagamentos que simula a integração com múltiplos provedores (FastPay e SecurePay), aplicando regras de seleção automática, fallback em caso de falha e cálculo de taxas. Desenvolvido com FastAPI e Docker.

---

# Funcionalidades

- Recebe requisições de pagamento via JSON
- Seleciona automaticamente o provedor com base no valor
- Aplica taxas específicas por provedor
- Realiza fallback para outro provedor se o principal estiver indisponível
- Retorna valores brutos, taxas e líquidos com precisão de duas casas decimais

---

##  Tecnologias

- Python
- FastAPI
- Docker / Docker Compose
- Uvicorn

---

##  Como rodar localmente

- Copiar o porjeto do GIT
- Instalar Docker
- Rodar o Docker Compose

