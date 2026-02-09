"""Screen capture functionality for the AI Assistant"""
from PIL import ImageGrab
import os
from datetime import datetime


class ScreenCapture:
    """Handles screen capturing and image processing"""
    
    def __init__(self):
        self.screenshots_dir = "screenshots"
        self._create_screenshots_dir()
    
    def _create_screenshots_dir(self):
        """Create screenshots directory if it doesn't exist"""
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
    
    def capture_screen(self, save=False):
        """
        Capture the current screen
        
        Args:
            save (bool): Whether to save the screenshot to disk
            
        Returns:
            PIL.Image: The captured screenshot
        """
        try:
            screenshot = ImageGrab.grab()
            
            if save:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(self.screenshots_dir, f"screenshot_{timestamp}.png")
                screenshot.save(filename)
                print(f"Screenshot saved: {filename}")
            
            return screenshot
        except Exception as e:
            print(f"Error capturing screen: {e}")
            return None
    
    def capture_area(self, bbox=None):
        """
        Capture a specific area of the screen
        
        Args:
            bbox (tuple): Bounding box (left, top, right, bottom)
            
        Returns:
            PIL.Image: The captured screenshot area
        """
        try:
            if bbox:
                screenshot = ImageGrab.grab(bbox=bbox)
            else:
                screenshot = ImageGrab.grab()
            return screenshot
        except Exception as e:
            print(f"Error capturing screen area: {e}")
            return None
