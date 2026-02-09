"""GUI for the AI Assistant using Tkinter"""
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from PIL import Image, ImageTk
import threading
from src.openai_handler import OpenAIHandler
from src.screen_capture import ScreenCapture
from src.voice_output import VoiceOutput
from src.config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE


class AIAssistantGUI:
    """Main GUI class for the AI Assistant"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        
        # Initialize components
        self.openai = OpenAIHandler()
        self.screen_capture = ScreenCapture()
        self.voice = VoiceOutput()
        self.conversation_history = []
        self.current_screenshot = None
        
        # UI setup
        self._setup_ui()
    
    def _setup_ui(self):
        """Set up the user interface"""
        # Top frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # Capture screenshot button
        self.capture_btn = tk.Button(
            button_frame,
            text="📷 Capture Screen",
            command=self._capture_screenshot,
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white"
        )
        self.capture_btn.pack(side=tk.LEFT, padx=5)
        
        # Voice toggle button
        self.voice_btn = tk.Button(
            button_frame,
            text="🔊 Voice ON",
            command=self._toggle_voice,
            font=("Arial", 10),
            bg="#2196F3",
            fg="white"
        )
        self.voice_btn.pack(side=tk.LEFT, padx=5)
        self.voice_enabled = True
        
        # Clear button
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self._clear_chat,
            font=("Arial", 10),
            bg="#FF9800",
            fg="white"
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Main content frame
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Screenshot preview
        preview_frame = tk.LabelFrame(content_frame, text="Screenshot Preview", font=("Arial", 9))
        preview_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.screenshot_label = tk.Label(
            preview_frame,
            text="No screenshot captured\nClick 'Capture Screen' to begin",
            bg="#f0f0f0",
            font=("Arial", 10)
        )
        self.screenshot_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Chat area
        chat_frame = tk.LabelFrame(content_frame, text="Chat", font=("Arial", 9))
        chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Arial", 9),
            state=tk.DISABLED,
            bg="white"
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_field = tk.Entry(
            input_frame,
            font=("Arial", 10),
            bg="white"
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.input_field.bind("<Return>", lambda e: self._send_message())
        
        self.send_btn = tk.Button(
            input_frame,
            text="Send ➤",
            command=self._send_message,
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white"
        )
        self.send_btn.pack(side=tk.RIGHT)
    
    def _capture_screenshot(self):
        """Capture the screen"""
        def capture_task():
            self.capture_btn.config(state=tk.DISABLED)
            self.current_screenshot = self.screen_capture.capture_screen()
            
            if self.current_screenshot:
                # Resize for preview
                thumb = self.current_screenshot.copy()
                thumb.thumbnail((300, 300))
                
                photo = ImageTk.PhotoImage(thumb)
                self.screenshot_label.config(image=photo, text="")
                self.screenshot_label.image = photo
                
                self._add_to_chat("System", "Screenshot captured successfully!")
            else:
                messagebox.showerror("Error", "Failed to capture screenshot")
            
            self.capture_btn.config(state=tk.NORMAL)
        
        thread = threading.Thread(target=capture_task)
        thread.daemon = True
        thread.start()
    
    def _send_message(self):
        """Send message to AI"""
        message = self.input_field.get().strip()
        if not message:
            return
        
        self.input_field.delete(0, tk.END)
        self._add_to_chat("You", message)
        
        def process_message():
            self.send_btn.config(state=tk.DISABLED)
            
            if self.current_screenshot:
                response = self.openai.analyze_screenshot(self.current_screenshot, message)
            else:
                response, self.conversation_history = self.openai.chat(
                    message,
                    self.conversation_history
                )
            
            self._add_to_chat("AI Assistant", response)
            
            if self.voice_enabled:
                self.voice.speak(response)
            
            self.send_btn.config(state=tk.NORMAL)
        
        thread = threading.Thread(target=process_message)
        thread.daemon = True
        thread.start()
    
    def _add_to_chat(self, sender, message):
        """Add message to chat display"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def _toggle_voice(self):
        """Toggle voice output"""
        self.voice_enabled = not self.voice_enabled
        status = "ON" if self.voice_enabled else "OFF"
        self.voice_btn.config(text=f"🔊 Voice {status}")
    
    def _clear_chat(self):
        """Clear chat history"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.conversation_history = []
        self._add_to_chat("System", "Chat cleared. Ready for new conversation!")
