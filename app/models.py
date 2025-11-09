from decimal import Decimal, ROUND_HALF_UP
from pydantic import BaseModel, EmailStr
from typing import Optional

class Payer(BaseModel):
    email: EmailStr

class PaymentRequest(BaseModel):
    amount: float
    currency: str
    payer: Optional[Payer] = None
    installments: Optional[int] = 1
    description: Optional[str] = None

def select_provider(amount: float) -> str:
    return "FastPay" if amount < 100 else "SecurePay"

def round_two(value: float) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def calculate_fee(amount: float, provider: str) -> float:
    if provider == "FastPay":
        return round_two(amount * 0.0349)
    else:
        return round_two(amount * 0.0299 + 0.40)
