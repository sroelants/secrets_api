from datetime import datetime
from app.models import Secret


def test_db_fixture(test_db):
    """
    GIVEN: A test database
    WHEN: Retrieving one of the preset users
    THEN: I find it in the db
    """
    assert Secret.query.all() != []


def test_adding_secret(test_db):
    """
    GIVEN: A test database
    WHEN: Adding a secret
    THEN: We find the secret in the db
    """
    secret = Secret("This is a new secret", datetime.now(), 0)
    test_db.session.add(secret)
    test_db.session.commit()
    assert Secret.query.all()[-1] == secret


def test_removing_secret(test_db):
    """
    GIVEN: A prepopulated db
    WHEN: I delete a secret
    THEN: It is no longer in the db
    """
    secret = Secret.query.first()
    test_db.session.delete(secret)
    test_db.session.commit()
    assert Secret.query.get(secret.id) is None
