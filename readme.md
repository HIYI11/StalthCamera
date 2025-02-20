# 📸 Telegram Photo Capture and Send Bot 🤖

This project captures an image from your webcam and sends it via a Telegram bot. The script automatically captures an image and sends it to a specified Telegram chat at a scheduled time using **Windows Task Scheduler**. 🌟

## Features ✨

- **Webcam Image Capture**: Automatically takes a snapshot from your webcam. 📷
- **Telegram Integration**: Sends captured images directly to your Telegram chat. 💬
- **Scheduled Execution**: Runs the script at specified times using Windows Task Scheduler. ⏰

## Requirements ✅

- Python 3.x
- `opencv-python` library
- `requests` library
- Telegram Bot Token and Chat ID

## Quick Start 🚀

1. **Install Required Libraries**:
   ```bash
   pip install opencv-python requests
   ```

2. **Create a Telegram Bot**:
   - Start a chat with [BotFather](https://t.me/botfather) on Telegram.
   - Create a new bot using the `/newbot` command.
   - Note down the provided Bot Token.

3. **Get Your Chat ID**:
   - Send a message to your bot and check the API response to find your Chat ID.

4. **Configure the Script**:
   Modify `StealthCamera.py` with your Bot Token and Chat ID:
   ```python
   BOT_TOKEN = 'your_bot_token_here'
   CHAT_ID = 'your_chat_id_here'
   ```

5. **Run the Script**:
   ```bash
   python StealthCamera.py
   ```

6. **Set Up Windows Task Scheduler**:
   Follow the instructions below to automate the script execution.

## Detailed Setup 🛠️

### 1. Telegram Bot Configuration 🤖

1. Open Telegram and search for "BotFather".
2. Start a chat and type `/newbot`.
3. Choose a name for your bot (e.g., "MyBot").
4. Copy your Bot Token for later use.

Creating Telegram Bot

### 2. Script Configuration ✍️

Modify `StealthCamera.py` with your Bot Token and Chat ID:

```python
BOT_TOKEN = 'your_bot_token_here'
CHAT_ID = 'your_chat_id_here'
```

### 3. Windows Task Scheduler Setup 🗓️

1. Open Task Scheduler (`taskschd.msc`).
2. Create a new task named "Telegram Photo Capture".
3. Configure it to run with highest privileges.
4. Set trigger for desired schedule (daily, weekly, etc.).
5. Add action to run `pythonw.exe` with the script path as an argument.

## Troubleshooting 🔧

If you encounter any issues, consider the following troubleshooting steps:

- Ensure that your webcam is properly connected and recognized by your computer.
- Verify that the Bot Token and Chat ID in your script are correct.
- Check if the required Python libraries (`opencv-python` and `requests`) are installed correctly.
- Review Task Scheduler settings to ensure the task is configured correctly.
- Check Task Scheduler history for any errors or warnings.

If problems persist, consult documentation for the libraries used or seek help from community forums! 🌐

## Contributing 🤝

Contributions are welcome! Feel free to submit a Pull Request with improvements or enhancements.

## License 📄

This project is open source and available under the [MIT License](LICENSE).

