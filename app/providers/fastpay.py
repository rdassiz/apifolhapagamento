# providers/fastpay.py
from .base import PaymentProvider

class FastPay(PaymentProvider):
    def send_payment(self, payload: dict) -> dict:
        request = {
            "transaction_amount": payload["amount"],
            "currency": payload["currency"],
            "payer": payload["payer"],
            "installments": payload["installments"],
            "description": payload["description"]
        }
        return {
            "externalId": "FP-884512",
            "status": "approved",
            "provider": "FastPay"
        }
