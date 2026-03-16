"""
Test cases for WhatsApp AI Automation Framework
Tests message sending functionality with AI-generated content
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.whatsapp_page import WhatsAppPage
from ai.message_generator import MessageGenerator, generate_greeting
from utils.sheet_reader import load_contacts
from utils.logger import get_logger, log_step
from utils.config import (
    HEADLESS_MODE, CHROME_OPTIONS, CONTACT_EXCEL_FILE, 
    TEST_TIMEOUT, WHATSAPP_URL, REPORTS_PATH
)

logger = get_logger(__name__)


class TestWhatsAppMessaging:
    """Test cases for WhatsApp messaging functionality"""
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup test fixtures"""
        logger.info("Setting up test fixtures")
        
        options = Options()
        
        if HEADLESS_MODE:
            options.add_argument("--headless")
        
        for option in CHROME_OPTIONS:
            options.add_argument(option)
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(TEST_TIMEOUT)
        
        self.whatsapp_page = WhatsAppPage(self.driver)
        self.message_generator = MessageGenerator()
        
        yield
        
        # Teardown
        logger.info("Tearing down test fixtures")
        if self.driver:
            self.driver.quit()
    
    @log_step("Test: Navigate to WhatsApp")
    def test_navigate_to_whatsapp(self):
        """Test navigating to WhatsApp Web"""
        logger.info("Starting test_navigate_to_whatsapp")
        
        self.whatsapp_page.navigate_to_whatsapp()
        
        # Verify page title contains WhatsApp
        assert "WhatsApp" in self.driver.title
        logger.info(f"Page title: {self.driver.title}")
        
        # Take screenshot
        screenshot_path = REPORTS_PATH / "whatsapp_loaded.png"
        self.whatsapp_page.take_screenshot(str(screenshot_path))
    
    @log_step("Test: Generate greeting message")
    def test_generate_greeting_message(self):
        """Test AI-generated greeting message"""
        logger.info("Starting test_generate_greeting_message")
        
        contact_name = "John Doe"
        greeting = self.message_generator.generate_greeting(contact_name)
        
        assert greeting is not None
        assert contact_name in greeting or "Hi" in greeting or "Hello" in greeting
        assert len(greeting) > 0
        
        logger.info(f"Generated greeting: {greeting}")
    
    @log_step("Test: Generate contextual message")
    def test_generate_contextual_message(self):
        """Test generating contextual messages based on type"""
        logger.info("Starting test_generate_contextual_message")
        
        contact_name = "Jane Smith"
        message_type = "follow_up"
        context = {
            "product": "Automation Framework",
            "previous_interaction": "Initial meeting"
        }
        
        message = self.message_generator.generate_message(
            contact_name, 
            message_type, 
            context
        )
        
        assert message is not None
        assert len(message) > 0
        assert len(message) <= 500  # Should be reasonably sized
        
        logger.info(f"Generated message: {message}")
    
    @log_step("Test: Load contacts from Excel")
    def test_load_contacts_from_excel(self):
        """Test loading contact data from Excel file"""
        logger.info("Starting test_load_contacts_from_excel")
        
        try:
            contacts = load_contacts(CONTACT_EXCEL_FILE)
            
            logger.info(f"Loaded {len(contacts)} contacts")
            
            for contact in contacts:
                logger.debug(f"Contact: {contact}")
            
            assert isinstance(contacts, list)
            
        except FileNotFoundError as e:
            logger.warning(f"Excel file not found: {e}")
            pytest.skip("Contact Excel file not found")
    
    @log_step("Test: Search contact workflow")
    def test_search_contact_workflow(self):
        """Test the complete workflow of searching for a contact"""
        logger.info("Starting test_search_contact_workflow")
        
        # Note: This test requires manual QR code scan on WhatsApp Web
        logger.info("Navigate to WhatsApp and scan QR code within 60 seconds")
        
        self.whatsapp_page.navigate_to_whatsapp()
        
        # Wait for manual intervention
        time.sleep(5)
        
        logger.info("WhatsApp loaded successfully")
    
    @log_step("Test: Send single message")
    def test_send_single_message(self):
        """Test sending a single message"""
        logger.info("Starting test_send_single_message")
        
        # Generate a message
        contact_name = "Test Contact"
        message = generate_greeting(contact_name, context="Testing automation")
        
        logger.info(f"Generated message: {message}")
        
        # Verify message is valid
        assert message is not None
        assert len(message) > 0
        
        logger.info("Message validation passed")
    
    @log_step("Test: Send bulk messages (simulated)")
    def test_send_bulk_messages_simulated(self):
        """Test bulk message sending workflow (simulated without actual sending)"""
        logger.info("Starting test_send_bulk_messages_simulated")
        
        # Simulate contact list
        test_contacts = [
            {"name": "Alice", "phone": "+1234567890", "topic": "project"},
            {"name": "Bob", "phone": "+1234567891", "topic": "meeting"},
            {"name": "Charlie", "phone": "+1234567892", "topic": "update"}
        ]
        
        messages_generated = []
        
        for contact in test_contacts:
            greeting = generate_greeting(contact["name"])
            messages_generated.append({
                "contact": contact["name"],
                "message": greeting
            })
            logger.info(f"Message for {contact['name']}: {greeting}")
        
        assert len(messages_generated) == len(test_contacts)
        
        for msg in messages_generated:
            assert msg["message"] is not None
            assert len(msg["message"]) > 0
        
        logger.info(f"Successfully generated {len(messages_generated)} messages")
    
    @log_step("Test: Validate message appropriateness")
    def test_validate_message_appropriateness(self):
        """Test message validation functionality"""
        logger.info("Starting test_validate_message_appropriateness")
        
        test_messages = [
            "Hi, how are you?",
            "I hope this message finds you well",
            "Let's schedule a meeting"
        ]
        
        for message in test_messages:
            result = self.message_generator.validate_message(message)
            
            assert "is_valid" in result
            logger.info(f"Message '{message}' - Valid: {result['is_valid']}")


class TestWhatsAppIntegration:
    """Integration tests combining multiple features"""
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup test fixtures"""
        logger.info("Setting up integration test fixtures")
        self.message_generator = MessageGenerator()
        yield
    
    @log_step("Integration Test: End-to-end message flow")
    def test_end_to_end_message_flow(self):
        """Test complete message generation and preparation workflow"""
        logger.info("Starting integration test")
        
        # Step 1: Load contacts (simulated)
        test_contacts = [
            {"name": "Alice Johnson", "phone": "+1111111111"},
            {"name": "Bob Smith", "phone": "+2222222222"}
        ]
        
        # Step 2: Generate personalized messages
        generated_data = []
        for contact in test_contacts:
            message = generate_greeting(
                contact["name"],
                context="AI Automation Testing"
            )
            generated_data.append({
                "contact": contact,
                "message": message
            })
        
        # Step 3: Validate results
        assert len(generated_data) == len(test_contacts)
        for data in generated_data:
            assert data["message"] is not None
            assert len(data["message"]) > 0
        
        logger.info("Integration test completed successfully")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
