from app import create_app
from app import db
from app.models import Secret

app = create_app()

with app.app_context():
    db.create_all()
