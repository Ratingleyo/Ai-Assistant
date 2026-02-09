"""Voice output functionality for the AI Assistant"""
import pyttsx3
import threading


class VoiceOutput:
    """Handles text-to-speech functionality"""
    
    def __init__(self):
        self.engine = pyttsx3.init()
        self.is_speaking = False
        self._configure_engine()
    
    def _configure_engine(self):
        """Configure the text-to-speech engine"""
        from src.config import VOICE_RATE
        
        self.engine.setProperty('rate', VOICE_RATE)
        
        # Try to set a good voice
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
    
    def speak(self, text, async_mode=True):
        """
        Convert text to speech
        
        Args:
            text (str): The text to speak
            async_mode (bool): Whether to speak asynchronously
        """
        if async_mode:
            thread = threading.Thread(target=self._speak_sync, args=(text,))
            thread.daemon = True
            thread.start()
        else:
            self._speak_sync(text)
    
    def _speak_sync(self, text):
        """Internal method to perform synchronous speech"""
        try:
            self.is_speaking = True
            self.engine.say(text)
            self.engine.runAndWait()
            self.is_speaking = False
        except Exception as e:
            print(f"Error in voice output: {e}")
            self.is_speaking = False
    
    def stop(self):
        """Stop current speech"""
        try:
            self.engine.stop()
            self.is_speaking = False
        except Exception as e:
            print(f"Error stopping voice: {e}")
