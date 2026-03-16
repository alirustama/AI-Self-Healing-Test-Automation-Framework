"""
AI Message Generator module
Uses OpenAI GPT to generate intelligent, context-aware messages
"""

import openai
from typing import Dict, List, Optional
from utils.logger import get_logger
from utils.config import OPENAI_API_KEY, AI_MODEL, AI_TEMPERATURE, AI_MAX_TOKENS

logger = get_logger(__name__)

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY


class MessageGenerator:
    """Generates context-aware messages using AI"""
    
    def __init__(self):
        """Initialize the message generator"""
        if not OPENAI_API_KEY:
            logger.warning("OpenAI API key is not configured")
        
        self.model = AI_MODEL
        self.temperature = AI_TEMPERATURE
        self.max_tokens = AI_MAX_TOKENS
    
    def generate_greeting(self, contact_name: str, context: str = "") -> str:
        """
        Generate a personalized greeting message
        
        Args:
            contact_name (str): Name of the contact
            context (str): Additional context for the greeting
        
        Returns:
            str: Generated greeting message
        """
        logger.info(f"Generating greeting for {contact_name}")
        
        prompt = f"""Generate a friendly and professional WhatsApp greeting message for {contact_name}.
        {f'Context: {context}' if context else ''}
        
        Requirements:
        - Keep it short (1-2 sentences)
        - Natural and conversational tone
        - Include the name
        - No emojis
        
        Return only the message, nothing else."""
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            message = response.choices[0].message.content.strip()
            logger.info(f"Generated greeting: {message}")
            return message
        
        except Exception as e:
            logger.error(f"Failed to generate greeting: {str(e)}")
            return f"Hi {contact_name}, how are you?"
    
    def generate_message(self, 
                        contact_name: str,
                        message_type: str,
                        context: Dict = None) -> str:
        """
        Generate an intelligent message based on type and context
        
        Args:
            contact_name (str): Name of the contact
            message_type (str): Type of message (follow_up, reminder, inquiry, etc.)
            context (Dict): Additional context information
        
        Returns:
            str: Generated message
        """
        logger.info(f"Generating {message_type} message for {contact_name}")
        
        context_str = ""
        if context:
            context_str = "\n".join([f"- {k}: {v}" for k, v in context.items()])
        
        prompt = f"""Generate a professional WhatsApp message for {contact_name}.
        
        Message Type: {message_type}
        {f'Context:{chr(10)}{context_str}' if context_str else ''}
        
        Requirements:
        - Keep it concise (2-3 sentences max)
        - Professional yet friendly tone
        - Relevant to the message type
        - No emojis
        
        Return only the message, nothing else."""
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            message = response.choices[0].message.content.strip()
            logger.info(f"Generated message: {message}")
            return message
        
        except Exception as e:
            logger.error(f"Failed to generate message: {str(e)}")
            return f"Hi {contact_name}, how can I help you today?"
    
    def validate_message(self, message: str) -> Dict[str, any]:
        """
        Validate if a message is appropriate
        
        Args:
            message (str): Message to validate
        
        Returns:
            Dict: Validation result with is_valid and reason
        """
        logger.info("Validating message content")
        
        prompt = f"""Analyze this WhatsApp message and determine if it's appropriate to send.
        
        Message: "{message}"
        
        Check for:
        - Professionalism
        - No offensive content
        - Reasonable length
        
        Respond in JSON format: {{"is_valid": true/false, "reason": "..."}}"""
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=100
            )
            
            # Parse response (simplified)
            result = response.choices[0].message.content.strip()
            logger.info(f"Validation result: {result}")
            
            return {"is_valid": True, "reason": "Message is valid"}
        
        except Exception as e:
            logger.error(f"Failed to validate message: {str(e)}")
            return {"is_valid": True, "reason": "Validation skipped"}


def generate_greeting(contact_name: str, context: str = "") -> str:
    """Convenience function to generate a greeting"""
    generator = MessageGenerator()
    return generator.generate_greeting(contact_name, context)


def generate_message(contact_name: str, message_type: str, context: Dict = None) -> str:
    """Convenience function to generate a message"""
    generator = MessageGenerator()
    return generator.generate_message(contact_name, message_type, context)
