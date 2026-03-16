"""
WhatsApp Page Object Model
Defines all page elements and interactions for WhatsApp Web
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import Optional
from utils.logger import get_logger
from utils.config import EXPLICIT_WAIT, WHATSAPP_URL

logger = get_logger(__name__)


class WhatsAppPage:
    """Page Object Model for WhatsApp Web interface"""
    
    # Locators
    SEARCH_BOX = (By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
    CHAT_INPUT = (By.XPATH, "//div[@contenteditable='true'][@data-tab='1']")
    SEND_BUTTON = (By.XPATH, "//button[@aria-label='Send']")
    CONTACT_NAME = (By.XPATH, "//span[@dir='auto'][@title]")
    CHAT_MESSAGE = (By.XPATH, "//div[@class='message-in']//span[@class='selectable-text']")
    QR_CODE = (By.XPATH, "//canvas[@aria-label='Scan this QR code to link a device!']")
    LOADING_SPINNER = (By.XPATH, "//div[@class='spinner']")
    NO_CHAT_SELECTED = (By.XPATH, "//div[@class='no-select']")
    
    def __init__(self, driver: webdriver.Chrome):
        """
        Initialize WhatsApp Page Object
        
        Args:
            driver (webdriver.Chrome): Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
        logger.info("WhatsApp Page Object initialized")
    
    def navigate_to_whatsapp(self) -> None:
        """Navigate to WhatsApp Web"""
        logger.info(f"Navigating to {WHATSAPP_URL}")
        self.driver.get(WHATSAPP_URL)
        self._wait_for_page_load()
    
    def _wait_for_page_load(self) -> None:
        """Wait for WhatsApp page to load"""
        try:
            # Check for QR code or main interface
            self.wait.until(
                EC.presence_of_element_located(self.QR_CODE)
            )
            logger.info("QR code detected - awaiting scan")
        except:
            logger.info("QR code not found - page may already be loaded")
    
    def search_contact(self, contact_name: str) -> None:
        """
        Search for a contact by name
        
        Args:
            contact_name (str): Name of the contact to search for
        """
        logger.info(f"Searching for contact: {contact_name}")
        
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located(self.SEARCH_BOX)
            )
            search_box.click()
            search_box.send_keys(contact_name)
            
            # Wait for search results
            import time
            time.sleep(1)
            
            logger.info(f"Successfully searched for {contact_name}")
        except Exception as e:
            logger.error(f"Failed to search contact: {str(e)}")
            raise
    
    def select_contact(self, contact_name: str) -> None:
        """
        Select a contact from search results
        
        Args:
            contact_name (str): Name of the contact to select
        """
        logger.info(f"Selecting contact: {contact_name}")
        
        try:
            # Click on the first contact result
            contact = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, 
                    f"//span[@title='{contact_name}']"
                ))
            )
            contact.click()
            logger.info(f"Successfully selected {contact_name}")
        except Exception as e:
            logger.error(f"Failed to select contact: {str(e)}")
            raise
    
    def send_message(self, message: str) -> None:
        """
        Send a message to the active chat
        
        Args:
            message (str): Message text to send
        """
        logger.info(f"Sending message: {message[:50]}...")
        
        try:
            # Click on message input field
            chat_input = self.wait.until(
                EC.presence_of_element_located(self.CHAT_INPUT)
            )
            chat_input.click()
            
            # Type message
            chat_input.send_keys(message)
            
            # Send message
            send_button = self.wait.until(
                EC.element_to_be_clickable(self.SEND_BUTTON)
            )
            send_button.click()
            
            logger.info("Message sent successfully")
        except Exception as e:
            logger.error(f"Failed to send message: {str(e)}")
            raise
    
    def send_message_to_contact(self, contact_name: str, message: str) -> None:
        """
        Search for a contact and send a message
        
        Args:
            contact_name (str): Name of the contact
            message (str): Message to send
        """
        logger.info(f"Sending message to {contact_name}")
        
        try:
            self.search_contact(contact_name)
            self.select_contact(contact_name)
            self.send_message(message)
            logger.info(f"Successfully sent message to {contact_name}")
        except Exception as e:
            logger.error(f"Failed to send message to {contact_name}: {str(e)}")
            raise
    
    def get_last_message(self) -> Optional[str]:
        """
        Get the last message in the current chat
        
        Returns:
            str: Last message text or None
        """
        try:
            messages = self.driver.find_elements(*self.CHAT_MESSAGE)
            if messages:
                last_message = messages[-1].text
                logger.info(f"Last message: {last_message}")
                return last_message
            return None
        except Exception as e:
            logger.error(f"Failed to get last message: {str(e)}")
            return None
    
    def clear_chat_input(self) -> None:
        """Clear the chat input field"""
        try:
            chat_input = self.driver.find_element(*self.CHAT_INPUT)
            chat_input.send_keys(Keys.CONTROL + "a")
            chat_input.send_keys(Keys.DELETE)
            logger.info("Chat input cleared")
        except Exception as e:
            logger.error(f"Failed to clear chat input: {str(e)}")
    
    def take_screenshot(self, filename: str) -> None:
        """
        Take a screenshot of the current page
        
        Args:
            filename (str): Filename for the screenshot
        """
        try:
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")
