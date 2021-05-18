import pytest

from api import app_factory, config


@pytest.fixture
def app():
    
    app = app_factory.create_app(settings=config.dev_config)
    with app.app_context():
        yield app
        
        
@pytest.fixture
def test_client_fixture(app):
    
    with app.test_client() as test_client:
        yield test_client