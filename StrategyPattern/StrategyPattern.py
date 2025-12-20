from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PaypalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} paid using paypal")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} paid using credit card")

class PaytmPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} paid using paytm")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} paid using debit card")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def setStrategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def makePayment(self, amount):
        self._strategy.pay(amount=amount)

if __name__ == "__main__":
    payment = PaymentContext(CreditCardPayment())
    payment.makePayment(1500)

    payment.setStrategy(DebitCardPayment())
    payment.makePayment(2500)

    payment.setStrategy(PaytmPayment())
    payment.makePayment(4000)

