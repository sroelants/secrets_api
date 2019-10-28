from app.models import Secret
from datetime import datetime


def test_creating_secret():
    """
    GIVEN: A Secret model
    WHEN: I create a secret using the constructor
    THEN: It creates without error
    """
    secret = Secret("This is a secret", datetime.now(), 0)
    assert secret.secret == "This is a secret"
    assert secret.likes == 0
