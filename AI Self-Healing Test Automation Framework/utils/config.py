"""
Configuration module for WhatsApp AI Automation Framework
Handles all configuration settings and environment variables
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
TEST_DATA_PATH = PROJECT_ROOT / "test_data"
REPORTS_PATH = PROJECT_ROOT / "reports"
LOGS_PATH = PROJECT_ROOT / "logs"

# Create necessary directories
LOGS_PATH.mkdir(exist_ok=True)
REPORTS_PATH.mkdir(exist_ok=True)

# Browser Configuration
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS_MODE = os.getenv("HEADLESS_MODE", "False").lower() == "true"
BROWSER_WINDOW_SIZE = os.getenv("BROWSER_WINDOW_SIZE", "1920,1080")
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))

# Chrome Driver Configuration
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", None)
CHROME_OPTIONS = [
    "--disable-blink-features=AutomationControlled",
    "--disable-extensions",
    "--disable-dev-shm-usage",
    "--no-sandbox",
]

# WhatsApp Configuration
WHATSAPP_URL = os.getenv("WHATSAPP_URL", "https://web.whatsapp.com")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER", "")
CONTACT_EXCEL_FILE = os.getenv("CONTACT_EXCEL_FILE", str(TEST_DATA_PATH / "contacts.xlsx"))

# AI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "gpt-3.5-turbo")
AI_TEMPERATURE = float(os.getenv("AI_TEMPERATURE", "0.7"))
AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", "150"))

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = LOGS_PATH / "automation.log"

# Test Configuration
TEST_TIMEOUT = int(os.getenv("TEST_TIMEOUT", "60"))
RETRY_COUNT = int(os.getenv("RETRY_COUNT", "3"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "2"))

# Features
ENABLE_SELF_HEALING = os.getenv("ENABLE_SELF_HEALING", "True").lower() == "true"
ENABLE_SCREENSHOTS = os.getenv("ENABLE_SCREENSHOTS", "True").lower() == "true"
SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "True").lower() == "true"

# Report Configuration
REPORT_FORMAT = os.getenv("REPORT_FORMAT", "html")
REPORT_FILE_PATH = REPORTS_PATH / "report.html"

# Validation
if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not set in environment variables")

if not WHATSAPP_NUMBER:
    print("Warning: WHATSAPP_NUMBER not set in environment variables")
