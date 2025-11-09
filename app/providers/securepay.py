# providers/securepay.py
from .base import PaymentProvider

class SecurePay(PaymentProvider):
    def send_payment(self, payload: dict) -> dict:
        request = {
            "amount_cents": int(payload["amount"] * 100),
            "currency_code": payload["currency"],
            "client_reference": payload["client_reference"]
        }
        return {
            "externalId": "SP-19283",
            "status": "approved",
            "provider": "SecurePay"
        }