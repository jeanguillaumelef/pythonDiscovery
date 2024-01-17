# routes.py
from flask import Blueprint, request
from payment_service import PaymentService
from payment_repository import PaymentRepository

bp = Blueprint('routes', __name__)
payment_service = PaymentService(PaymentRepository())

@bp.route('/payments', methods=['POST'])
def receive_payment():
    data = request.json
    payment = payment_service.create_payment(data)
    return {'id': payment.id}, 201