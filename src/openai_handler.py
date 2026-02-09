"""OpenAI API integration for the AI Assistant"""
from openai import OpenAI
import base64
from io import BytesIO
from PIL import Image
from src.config import OPENAI_API_KEY, MODEL


class OpenAIHandler:
    """Handles all OpenAI API interactions"""
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = MODEL
    
    def image_to_base64(self, image):
        """
        Convert PIL Image to base64 string
        
        Args:
            image (PIL.Image): The image to convert
            
        Returns:
            str: Base64 encoded image string
        """
        if isinstance(image, Image.Image):
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            return img_base64
        return None
    
    def analyze_screenshot(self, image, prompt):
        """
        Analyze a screenshot using GPT-4 Vision
        
        Args:
            image (PIL.Image): The screenshot to analyze
            prompt (str): The user's prompt/question
            
        Returns:
            str: The AI's response
        """
        try:
            base64_image = self.image_to_base64(image)
            
            if not base64_image:
                return "Error: Could not process image"
            
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": base64_image,
                                },
                            },
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ],
                    }
                ],
            )
            
            return response.content[0].text
        except Exception as e:
            return f"Error analyzing screenshot: {str(e)}"
    
    def chat(self, message, conversation_history=None):
        """
        Send a text message to the AI
        
        Args:
            message (str): The user's message
            conversation_history (list): Previous messages in conversation
            
        Returns:
            str: The AI's response
        """
        try:
            if conversation_history is None:
                conversation_history = []
            
            conversation_history.append({
                "role": "user",
                "content": message
            })
            
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=conversation_history
            )
            
            ai_response = response.content[0].text
            conversation_history.append({
                "role": "assistant",
                "content": ai_response
            })
            
            return ai_response, conversation_history
        except Exception as e:
            return f"Error in chat: {str(e)}", conversation_history
