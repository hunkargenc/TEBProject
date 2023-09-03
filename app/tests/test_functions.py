from unittest.mock import patch

import pytest

from app.apis.api_v1.prediction import sentiment_prediction as sentiment_func
from app.apis.api_v1.prediction import intention_prediction as intention_func


@pytest.fixture(scope="module")
def mock_get_data():
    """Mock get_data function."""

    with patch("app.apis.api_v1.utils.get_data", return_value=42, auto=True) as m:
        yield m
