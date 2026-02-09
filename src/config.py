"""Configuration and constants for the AI Assistant"""
import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL = "gpt-4-vision-preview"

# GUI Configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "AI Assistant"

# Screen Capture Configuration
SCREENSHOT_QUALITY = 95
MAX_IMAGE_SIZE = (2560, 1080)

# Voice Configuration
VOICE_ENABLED = True
VOICE_RATE = 150  # Words per minute
