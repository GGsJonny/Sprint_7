import pytest
import helpers


@pytest.fixture
def courier_credentials():
    credentials = helpers.create_courier()

    yield credentials

    helpers.delete_courier(credentials)


@pytest.fixture
def created_courier_credentials():
    credentials = helpers.create_courier(register=True)

    yield credentials

    helpers.delete_courier(credentials)