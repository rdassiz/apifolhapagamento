from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def send_payment(self, payload: dict) -> dict:
        """Sends a payment request to the provider."""
        raise NotImplementedError("Método não implementado.")