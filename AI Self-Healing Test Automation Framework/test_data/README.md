# WhatsApp AI Automation Test Data

This directory contains test data files for the automation framework.

## Files

- **contacts.xlsx** - Contact list for testing message sending

## Format

### contacts.xlsx
Columns:
- Name: Contact name
- Phone: Phone number
- Email: Email address
- Company: Company name (optional)
- Notes: Additional notes (optional)

Example:
| Name | Phone | Email | Company | Notes |
|------|-------|-------|---------|-------|
| John Doe | +1234567890 | john@example.com | Tech Corp | VIP Client |
| Jane Smith | +1234567891 | jane@example.com | Startup Inc | Follow up |

## Usage

The framework automatically loads contacts from `contacts.xlsx` for testing bulk messaging functionality.

## Creating Sample Data

1. Use Excel or Google Sheets to create the contact list
2. Save as `.xlsx` format
3. Place in this directory
4. Update `CONTACT_EXCEL_FILE` in `.env` if using a different filename
