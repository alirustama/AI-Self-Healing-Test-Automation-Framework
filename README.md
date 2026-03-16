# AI-Self-Healing-Test-Automation-Framework
# WhatsApp web AI Automation Framework

An intelligent test automation framework that combines Selenium WebDriver with AI capabilities to automate WhatsApp messaging workflows, including self-healing features for robust testing.

## Features

- **AI-Powered Message Generation**: Generates contextually appropriate messages using GPT/OpenAI
- **Page Object Model**: Structured approach to WhatsApp interaction
- **Excel Data Integration**: Load test data from Excel files
- **Self-Healing**: Smart element detection and recovery
- **Comprehensive Logging**: Detailed logs for debugging and reporting
- **CI/CD Integration**: GitHub Actions workflow for automated testing
- **HTML Reports**: Beautiful test execution reports

## Project Structure

```
whatsapp-ai-automation/
├── tests/                 # Test cases
├── pages/                 # Page Object Models
├── ai/                    # AI integration modules
├── utils/                 # Utility functions
├── test_data/             # Test data (Excel files)
├── reports/               # Test reports
├── .github/workflows/     # CI/CD pipelines
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd whatsapp-ai-automation
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with HTML report
pytest tests/ --html=reports/report.html

# Run specific test
pytest tests/test_send_messages.py::test_send_single_message
```

### Example Test
```python
from tests.test_send_messages import TestWhatsAppMessaging

test = TestWhatsAppMessaging()
test.setup_method()
test.test_send_single_message()
```

## Configuration

Edit `utils/config.py` to configure:
- Browser settings
- Wait times
- Log level
- AI endpoints
- Excel file paths

## Environment Variables

Create `.env` file:
```
OPENAI_API_KEY=your_api_key_here
WHATSAPP_NUMBER=your_number
CHROME_DRIVER_PATH=/path/to/chromedriver
LOG_LEVEL=INFO
```

## AI Integration

The framework uses OpenAI GPT to generate intelligent, context-aware messages:
- Automatically generates appropriate greetings
- Personalizes messages based on contact data
- Handles message variations

## CI/CD Pipeline

GitHub Actions automatically:
- Runs tests on push and PR
- Generates HTML reports
- Archives reports as artifacts

## Troubleshooting

### Common Issues

1. **ChromeDriver version mismatch**
   - Solution: `webdriver-manager` auto-downloads matching driver

2. **OpenAI API key not found**
   - Ensure `OPENAI_API_KEY` is set in `.env`

3. **Excel file not found**
   - Check file path in `utils/config.py`

## License

MIT License - see LICENSE file for details

## Contributing

1. Create feature branch
2. Make changes
3. Run tests
4. Submit pull request

## Support

For issues and questions, please open a GitHub issue.
