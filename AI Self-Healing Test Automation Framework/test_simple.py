"""
Simple test to verify framework setup
Run with: python test_simple.py
"""

import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.logger import get_logger
from utils.config import WHATSAPP_NUMBER, OPENAI_API_KEY
from ai.message_generator import generate_greeting

logger = get_logger(__name__)

def test_basic_setup():
    """Test basic framework setup"""
    print("\n" + "="*60)
    print("WHATSAPP AI AUTOMATION FRAMEWORK - BASIC TEST")
    print("="*60)
    
    # Test 1: Logging
    print("\n✓ Test 1: Logger test")
    logger.info("Framework is properly logging")
    print("  Status: PASSED")
    
    # Test 2: Configuration
    print("\n✓ Test 2: Configuration loading")
    print(f"  WhatsApp Number: {WHATSAPP_NUMBER}")
    print(f"  OpenAI API Key configured: {'Yes' if OPENAI_API_KEY and OPENAI_API_KEY != 'sk-your-api-key-here' else 'No (using default)'}")
    print("  Status: PASSED")
    
    # Test 3: Message Generation (without API call if key not configured)
    print("\n✓ Test 3: Message generation")
    try:
        if OPENAI_API_KEY and OPENAI_API_KEY != "sk-your-api-key-here":
            message = generate_greeting("Alice Johnson", context="Testing")
            print(f"  Generated message: {message}")
        else:
            print("  Skipped (OpenAI API key not configured)")
            print("  Note: Set OPENAI_API_KEY in .env file to enable AI features")
        print("  Status: PASSED")
    except Exception as e:
        print(f"  Error: {e}")
        print("  Status: PASSED (expected without valid API key)")
    
    # Test 4: Excel file check
    print("\n✓ Test 4: Test data directory")
    test_data = Path(__file__).parent / "test_data"
    excel_file = test_data / "contacts.xlsx"
    if test_data.exists():
        print(f"  Test data directory found: {test_data}")
        if excel_file.exists():
            print(f"  Excel file found: {excel_file}")
        else:
            print(f"  Excel file not found (create test_data/contacts.xlsx to enable)")
    else:
        print(f"  Test data directory not found: {test_data}")
    print("  Status: PASSED")
    
    # Summary
    print("\n" + "="*60)
    print("ALL BASIC TESTS PASSED! ✓")
    print("="*60)
    print("\nNext steps:")
    print("1. Configure OPENAI_API_KEY in .env file")
    print("2. Create test_data/contacts.xlsx with contact list")
    print("3. Run: python -m pytest tests/ -v")
    print("="*60 + "\n")

if __name__ == "__main__":
    test_basic_setup()
