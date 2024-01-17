# test_payment_service.py
from unittest.mock import Mock
from payment_service import PaymentService

def test_create_payment():
    mock_repository = Mock()
    service = PaymentService(mock_repository)
    data = {'amount': 100.0, 'method': 'credit card'}
    service.create_payment(data)
    mock_repository.save.assert_called_once_with({'amount': 100.0, 'method': 'credit card'})