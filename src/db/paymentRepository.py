# payment_repository.py
from database import db, Payment

class PaymentRepository:
    def save(self, data):
        payment = Payment(amount=data['amount'], method=data['method'])
        db.session.add(payment)
        db.session.commit()
        return payment