# payment_service.py
class PaymentService:
    def __init__(self, payment_repository):
        self.payment_repository = payment_repository

    def create_payment(self, data):        
        return self.payment_repository.save(data)