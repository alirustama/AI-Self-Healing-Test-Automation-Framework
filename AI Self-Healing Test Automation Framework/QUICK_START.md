# Quick Start Guide

## Prerequisites

- Python 3.9+
- Google Chrome browser
- WhatsApp account with web access enabled
- OpenAI API key (optional, for AI message generation)

## Installation Steps

### 1. Clone and Setup

```bash
# Navigate to project directory
cd whatsapp-ai-automation

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
# - Set your OpenAI API key
# - Configure browser options
# - Set test data paths
```

### 4. Prepare Test Data

1. Create `test_data/contacts.xlsx` with your contact list
2. Format: Name | Phone | Email | Company | Notes
3. Or use the sample data provided

## Running Tests

### Basic Test Run

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_send_messages.py

# Run specific test
pytest tests/test_send_messages.py::TestWhatsAppMessaging::test_generate_greeting_message
```

### Advanced Testing

```bash
# Run with HTML report
pytest tests/ --html=reports/report.html --self-contained-html

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run only unit tests
pytest tests/ -m "not requires_whatsapp"

# Run tests in parallel
pip install pytest-xdist
pytest tests/ -n auto
```

## Project Structure

```
├── tests/                 # Test cases
│   └── test_send_messages.py
├── pages/                 # Page Object Models
│   └── whatsapp_page.py
├── ai/                    # AI integration
│   └── message_generator.py
├── utils/                 # Utilities
│   ├── config.py
│   ├── logger.py
│   └── sheet_reader.py
├── test_data/             # Test data files
│   └── contacts.xlsx
├── reports/               # Test reports
├── .github/workflows/     # CI/CD
│   └── automation.yml
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
└── README.md             # Documentation
```

## Key Features

### 1. WhatsApp Page Object Model
- Structured interaction with WhatsApp Web
- Search, select, and message contacts
- Screenshot and logging capabilities

### 2. AI Message Generation
- GPT-powered intelligent message creation
- Context-aware personalization
- Message validation

### 3. Excel Data Integration
- Load contacts from Excel files
- Flexible schema support
- Error handling

### 4. Comprehensive Logging
- Colored console output
- File-based logging
- Decorator-based step tracking

### 5. CI/CD Integration
- GitHub Actions workflows
- Multi-version Python testing
- Automated reporting

## Common Tasks

### Add a New Test

1. Create test file in `tests/`
2. Import necessary modules
3. Use Page Object Model for interactions
4. Run: `pytest tests/test_new_file.py`

### Add a New Contact Field

1. Update Excel schema in `test_data/contacts.xlsx`
2. Modify parsing in `utils/sheet_reader.py` if needed
3. Use new field in tests

### Modify Configuration

1. Edit `.env` file
2. Or modify `utils/config.py` for default values
3. Restart tests

### Debug a Failing Test

1. Check logs in `logs/automation.log`
2. Check screenshots in `reports/`
3. Run with verbose: `pytest tests/ -v -s`
4. Use pdb: Add `import pdb; pdb.set_trace()` in code

## Troubleshooting

### ChromeDriver Issues
- `webdriver-manager` auto-downloads matching driver
- If still failing: manually download from chromedriver.chromium.org

### WhatsApp QR Code Not Appearing
- Try in incognito mode
- Clear browser cache
- Check internet connection

### OpenAI API Errors
- Verify API key in `.env`
- Check API rate limits
- Verify account balance

### Import Errors
- Activate virtual environment: `source venv/bin/activate` (or .bat on Windows)
- Reinstall dependencies: `pip install -r requirements.txt`
- Check PYTHONPATH includes project root

## Performance Tips

1. Use headless mode for CI/CD: `HEADLESS_MODE=True`
2. Adjust waits based on network: `EXPLICIT_WAIT=20`
3. Use markers to run subsets: `pytest -m "not slow"`
4. Parallel execution: `pytest -n auto`

## Next Steps

1. Read [README.md](README.md) for detailed documentation
2. Explore test examples in `tests/test_send_messages.py`
3. Review Page Object Model in `pages/whatsapp_page.py`
4. Check AI integration in `ai/message_generator.py`
5. Set up CI/CD by pushing to GitHub

## Support & Contributions

- Issues: Create GitHub issue with details
- Contributions: Fork, create feature branch, submit PR
- Documentation: Update README.md for changes
