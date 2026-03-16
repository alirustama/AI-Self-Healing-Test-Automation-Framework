"""
Pytest configuration and fixtures
Provides shared fixtures and configuration for all tests
"""

import pytest
from pathlib import Path

try:
    from utils.logger import get_logger
    logger = get_logger(__name__)
except Exception:
    logger = None


@pytest.fixture(scope="session")
def project_root():
    """Get the project root directory"""
    return Path(__file__).parent


@pytest.fixture(scope="session")
def test_data_path(project_root):
    """Get the test data directory"""
    return project_root / "test_data"


@pytest.fixture(scope="session")
def reports_path(project_root):
    """Get the reports directory"""
    path = project_root / "reports"
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture(scope="session")
def logs_path(project_root):
    """Get the logs directory"""
    path = project_root / "logs"
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture
def mock_contacts():
    """Provide mock contact data for testing"""
    return [
        {
            "name": "Alice Johnson",
            "phone": "+1234567890",
            "email": "alice@example.com",
            "company": "Tech Corp"
        },
        {
            "name": "Bob Smith",
            "phone": "+1234567891",
            "email": "bob@example.com",
            "company": "Startup Inc"
        },
        {
            "name": "Charlie Brown",
            "phone": "+1234567892",
            "email": "charlie@example.com",
            "company": "Enterprise Ltd"
        }
    ]


@pytest.fixture
def sample_messages():
    """Provide sample messages for testing"""
    return [
        "Hi, how are you doing?",
        "I hope this message finds you well",
        "Let's schedule a meeting to discuss this",
        "Thank you for your time",
        "Looking forward to hearing from you"
    ]


def pytest_configure(config):
    """Configure pytest"""
    if logger:
        logger.info("Pytest configuration started")
        logger.info(f"Test files: {config.getini('testpaths')}")


def pytest_sessionstart(session):
    """Called before test session starts"""
    if logger:
        logger.info("Test session started")


def pytest_sessionfinish(session, exitstatus):
    """Called after test session finishes"""
    if logger:
        logger.info(f"Test session finished with status: {exitstatus}")
