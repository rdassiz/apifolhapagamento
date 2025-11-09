# main.py
from fastapi import FastAPI, HTTPException
from app.providers.fastpay import FastPay
from app.providers.securepay import SecurePay
from app.payment_gateway import process_payment

app = FastAPI()

@app.post("/payments")
def create_payment(payload: dict):
    try:
        return process_payment(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))