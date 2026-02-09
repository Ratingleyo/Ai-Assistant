"""Main entry point for the AI Assistant Desktop App"""
import tkinter as tk
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.gui import AIAssistantGUI
from src.config import OPENAI_API_KEY


def main():
    """Main function to start the application"""
    # Check if API key is set
    if not OPENAI_API_KEY:
        print("WARNING: OPENAI_API_KEY not found. Please set it in .env file")
        print("Create a .env file with: OPENAI_API_KEY=your_api_key_here")
    
    # Create and run the GUI
    root = tk.Tk()
    app = AIAssistantGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
