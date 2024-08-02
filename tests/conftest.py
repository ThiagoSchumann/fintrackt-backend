import pytest
from app import create_app
from src import db

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db"  # Use SQLite para testes
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()
