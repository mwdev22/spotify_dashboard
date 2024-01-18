import pytest
from app import create_app, db as _db
import os

class TestConfig(object):
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db')  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(TestConfig)
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(scope='session')
def db(app):
    _db.app = app
    return _db

@pytest.fixture(scope='session')
def db_create(db):
    db.create_all()
    yield db  
    db.drop_all()  

@pytest.fixture
def db_session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
