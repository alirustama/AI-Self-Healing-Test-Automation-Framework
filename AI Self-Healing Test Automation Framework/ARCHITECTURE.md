# WhatsApp AI Automation - Architecture & Design

## System Architecture

```
┌─────────────────────┐
│   Test Cases        │
│  (pytest)           │
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     │            │
┌────▼────┐ ┌────▼────────┐
│  Pages   │ │ AI Generator │
│ (POM)    │ │ (GPT/OpenAI) │
└────┬────┘ └────┬────────┘
     │            │
     │    ┌───────┼────────┐
     │    │       │        │
┌────▼────▼──┐ ┌─▼───┐ ┌─▼──────┐
│  Selenium   │ │Utils│ │Logging │
│  WebDriver  │ │(POM)│ │Handler │
└────┬────────┘ └─────┘ └────────┘
     │
     ▼
┌──────────────────┐
│ WhatsApp Web     │
│ (Chrome)         │
└──────────────────┘
```

## Module Breakdown

### 1. **tests/** - Test Layer
- Contains all test cases using pytest
- Tests interact via Page Object Model
- Generates AI messages and validates behavior
- Includes unit, integration, and smoke tests

### 2. **pages/** - Page Object Model (POM)
- `WhatsAppPage`: Encapsulates WhatsApp Web interactions
- Methods for search, select, send messages
- Centralized element locators
- Exception handling & logging

### 3. **ai/** - AI Integration Layer
- `MessageGenerator`: GPT-powered message creation
- Greeting generation with personalization
- Context-aware message composition
- Message validation

### 4. **utils/** - Utility Modules
- `config.py`: Centralized configuration management
- `logger.py`: Structured logging with colors
- `sheet_reader.py`: Excel file parsing

## Data Flow

### Message Sending Flow
```
Test Case
    ↓
Load Contacts (Excel)
    ↓
Generate Message (AI)
    ↓
Navigate to WhatsApp
    ↓
Search Contact
    ↓
Select Contact
    ↓
Send Message
    ↓
Verify & Log Results
```

### Configuration Flow
```
.env File
    ↓
config.py (loads environment)
    ↓
All modules reference config
    ↓
Easy switching between environments
```

## Design Patterns Used

### 1. Page Object Model (POM)
- Encapsulates UI interactions
- Reduces test maintenance
- Improves code reusability

### 2. Decorator Pattern
- `@log_step` for test tracking
- Separates logging concern
- Maintains clean code

### 3. Factory Pattern
- `get_logger()` function
- `SheetReader` for files
- `MessageGenerator` for AI

### 4. Singleton Pattern
- Configuration (single instance)
- Logger instances per module

## Error Handling Strategy

```
Try Block
    │
    ├─► Selenium Operations (wait, find, click)
    ├─► API Calls (OpenAI)
    ├─► File Operations (Excel)
    │
Except Blocks
    │
    ├─► Log Error
    ├─► Take Screenshot (if enabled)
    ├─► Re-raise for test failure
    │
Finally
    └─► Cleanup resources
```

## Logging Strategy

### Log Levels
- **DEBUG**: Detailed information for debugging
- **INFO**: General operational flow
- **WARNING**: Warning messages (API key missing)
- **ERROR**: Error messages (failed operations)
- **CRITICAL**: Critical failures

### Log Destinations
- **Console**: Live colored output
- **File**: logs/automation.log
- **Test Report**: HTML report with timestamps

## Extension Points

### Adding New Tests
1. Create test class in `tests/`
2. Use `WhatsAppPage` for interactions
3. Use `MessageGenerator` for AI
4. Use decorators for logging

### Adding New Utilities
1. Create module in `utils/`
2. Add configuration in `config.py`
3. Use logging from `logger.py`

### Customizing AI Behavior
1. Modify prompts in `MessageGenerator`
2. Adjust temperature & tokens in `config.py`
3. Add validation rules

### Adding Databases
1. Create new module in `utils/`
2. Follow logger pattern
3. Update config.py
4. Reference in tests

## Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Test Framework | pytest | 7.4.3+ |
| Browser Automation | Selenium | 4.15.2+ |
| AI Integration | OpenAI API | Latest |
| Data Handling | openpyxl | 3.11.0+ |
| Environment | python-dotenv | 1.0.0+ |
| CI/CD | GitHub Actions | Latest |
| Python | CPython | 3.9+ |

## Performance Considerations

- **Wait Times**: Configurable via EXPLICIT_WAIT
- **Retry Logic**: Configurable via RETRY_COUNT
- **Headless Mode**: For CI/CD efficiency
- **Parallel Execution**: Support via pytest-xdist

## Security Considerations

- API keys in `.env` (not in repo)
- No credentials in logs
- Screenshots only on failure (optional)
- HTTPS for WhatsApp Web

## Scalability

- Multi-contact handling
- Batch message generation
- Parallel test execution
- Cloud-ready CI/CD

---

For more details, see [README.md](README.md) and [QUICK_START.md](QUICK_START.md)
