from datetime import datetime
import pytest
from app import create_app
from app.models import Secret
from config import TestingConfig


@pytest.fixture(scope='module')
def test_db():
    from app import db
    app = create_app(TestingConfig)
    with app.app_context():
        init_db(db)
        yield db
        db.drop_all()
        db.session.commit()


def init_db(db):
    db.create_all()
    secret1 = Secret("This is a first secret", datetime.now(), 0)
    secret2 = Secret("This is a second secret", datetime.now(), 0)
    secret3 = Secret("This is a third secret", datetime.now(), 0)
    db.session.add_all([secret1, secret2, secret3])


@pytest.fixture(scope='module')
def test_app(test_db):
    app = create_app(TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture(scope='module')
def test_client(test_app):
    yield test_app.test_client()
