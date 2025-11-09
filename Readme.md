# APIFolhaPagamento

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

| Camada         | Responsabilidade                                                                 |
|----------------|----------------------------------------------------------------------------------|
| API (FastAPI)  | Recebe requisições HTTP e valida o payload usando modelos Pydantic               |
| Modelos        | Define estrutura dos dados, regras de seleção de provedor e cálculo de taxas     |
| Orquestração   | Coordena o fluxo de pagamento, aplica fallback e formata a resposta final        |
| Provedores     | Implementa a lógica específica de cada provedor (FastPay, SecurePay)             |
| Infraestrutura | API via Docker Compose                                                           |

Fluxo de execução

1. requisição para `POST /payments`
2. FastAPI valida os dados com o modelo `PaymentRequest`
3. O sistema escolhe o provedor com base no valor 
4. Tenta enviar o pagamento com o provedor primário, se falhar, tenta outro provedor
6. Calcula taxa e valor líquido
7. Retorna



