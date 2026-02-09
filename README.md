# AI Assistant Desktop App

A Python desktop application that combines screen capture, AI conversation, and voice output into a simple, user-friendly interface.

## Features

- **Screen Capture**: Take screenshots and ask the AI about what's on your screen
- **AI Analysis**: Uses OpenAI's API (Claude 3.5 Sonnet) for intelligent responses
- **Text & Voice**: Get responses in both text form and spoken audio
- **Conversation Memory**: Maintains conversation history for context
- **Simple GUI**: Clean, intuitive Tkinter-based interface

## Requirements

- Python 3.8 or higher
- Windows/Mac/Linux
- OpenAI API key

## Installation

1. **Clone or download the project**
   ```bash
   cd AI Assistant
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the application:
```bash
python main.py
```

### Features in the GUI

1. **Capture Screen** - Takes a screenshot and displays a preview
2. **Ask Questions** - Ask the AI about the screenshot or anything else
3. **Voice Toggle** - Enable/disable voice output
4. **Clear Chat** - Clear conversation history
5. **Text Input** - Type your message and press Enter or click Send

## Project Structure

```
.
├── main.py                 # Entry point
├── requirements.txt        # Project dependencies
├── README.md              # This file
├── .env                   # API keys (create this)
├── .gitignore            # Git ignore file
├── .github/
│   └── copilot-instructions.md  # Development instructions
└── src/
    ├── __init__.py        # Package init
    ├── config.py          # Configuration constants
    ├── gui.py             # UI implementation
    ├── openai_handler.py  # OpenAI API integration
    ├── screen_capture.py  # Screen capture functionality
    └── voice_output.py    # Text-to-speech functionality
```

## Configuration

Edit `src/config.py` to customize:
- Window size and appearance
- Voice rate (words per minute)
- Screenshot quality
- Model selection

## Troubleshooting

### "OPENAI_API_KEY not found"
- Create a `.env` file with your API key
- Make sure the file is in the project root directory

### Voice not working
- Check if pyttsx3 and required audio libraries are installed
- On Linux, you may need to install espeak: `sudo apt-get install espeak`

### Screen capture issues
- On Mac, you may need to grant screen recording permissions
- Check System Preferences > Security & Privacy > Screen Recording

## Future Enhancements

- Auto-crop screen areas for better focus
- Save conversation history
- Multiple AI model support
- Custom hotkeys for quick capture
- Screenshot annotation tools
- Better error handling and logging

## License

MIT License - Feel free to use and modify as needed.

