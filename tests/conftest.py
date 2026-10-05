from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Provide a FastAPI TestClient for each test."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def restore_activities():
    """Restore the in-memory activity data after every test."""
    original_activities = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)
