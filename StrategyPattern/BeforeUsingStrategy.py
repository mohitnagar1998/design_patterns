class PaymentProcessor:
    def make_payment(self, payment_type: str, amount: int):
        # All payment logic is hardcoded in one method

        if payment_type == "creditcard":
            # credit card–specific logic
            print(f"{amount} paid using Credit Card")

        elif payment_type == "debitcard":
            # debit card–specific logic
            print(f"{amount} paid using Debit Card")

        elif payment_type == "paypal":
            # PayPal-specific logic
            print(f"{amount} paid using PayPal")

        elif payment_type == "paytm":
            # PayPal-specific logic
            print(f"{amount} paid using PayPal")

        else:
            print("Invalid payment type")


if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.make_payment("creditcard", 1500)
    processor.make_payment("debitcard", 2000)
    processor.make_payment("paypal", 2500)
    processor.make_payment("upi", 3000)   # invalid
