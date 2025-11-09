# paymentgateway.py
from app.providers.fastpay import FastPay
from app.providers.securepay import SecurePay
from app.models import calculate_fee, select_provider
from decimal import Decimal, ROUND_HALF_UP

def round_two(value: float) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def process_payment(payload: dict) -> dict:
    amount = payload["amount"]
    currency = payload["currency"]
    provider_name = select_provider(amount)

    providers = {
        "FastPay": FastPay(),
        "SecurePay": SecurePay()
    }

    primary = providers[provider_name]
    fallback = providers["SecurePay" if provider_name == "FastPay" else "FastPay"]

    for provider in [primary, fallback]:
        try:
            response = provider.send_payment(payload)
            fee = calculate_fee(amount, response["provider"])
            net_amount = round_two(amount - fee)

            return {
                "id": 1,
                "externalId": response["externalId"],
                "status": response["status"],
                "provider": response["provider"],
                "grossAmount": round_two(amount),
                "fee": round_two(fee),
                "netAmount": net_amount
            }
        except Exception:
            continue

    raise Exception("Nenhum provedor disponível")