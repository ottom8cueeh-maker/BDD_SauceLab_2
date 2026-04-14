"""Pytest configuration fixtures for the test suite.

Includes a `base_url` fixture which reads from the `BASE_URL` environment
variable or falls back to the Sauce Demo demo site.
"""

import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    """Base URL for tests. Use `BASE_URL` env var to override."""
    return os.environ.get("BASE_URL", "https://www.saucedemo.com")