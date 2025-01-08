# Telegram Photo Capture and Send Bot
This project captures an image from your webcam and sends it via a Telegram bot. The script automatically captures an image and sends it to a specified Telegram chat at a scheduled time using **Windows Task Scheduler**.

## Requirements

- Python 3.x
- `opencv-python` library
- `requests` library
- Telegram Bot Token and Chat ID

## Setup Instructions

### Step 1: Install Required Libraries

Before running the script, you need to install the necessary Python libraries. Open a terminal or command prompt and run the following commands:

```bash
pip install opencv-python requests
```

### Step 2: Create and Configure Your Telegram Bot

- Open Telegram and search for "BotFather".
- Start a chat with BotFather and type `/newbot`.
- Choose a name for your bot (e.g., "MyBot").
- BotFather will provide you with a Bot Token. Copy this token as you'll need it later in the script.

![Telegram Bot Creating](img/img1.png)

![Telegram Bot Creating](img/img2.png)

- Start a conversation with your newly created bot in Telegram (search for its name).
- Open this URL in your browser, replacing YOUR_BOT_TOKEN with the bot token you received from BotFather:

```
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```

- Send a message to your bot and refresh the previous page. In the response, find the `chat.id`. This is your Chat ID which the script will use to send messages to your Telegram chat. It looks like this:

```json
{
    "ok": true,
    "result": [
        {
            "update_id": 123456789,
            "message": {
                "message_id": 1,
                "from": {
                    "id": 123456789,
                    "is_bot": false,
                    "first_name": "John",
                    "last_name": "Doe",
                    "username": "johndoe",
                    "language_code": "en"
                },
                "chat": {
                    "id": 123456789,
                    "first_name": "John",
                    "last_name": "Doe",
                    "username": "johndoe",
                    "type": "private"
                },
                "date": 1620144065,
                "text": "Hello bot!"
            }
        }
    ]
}
```

- Download or create the Python script (e.g., `StealthCamera.py`) and modify it with your Bot Token and Chat ID.

### Step 3: Test the Script

- To test the script, simply run the Python file in your terminal or command prompt:

```bash
python StealthCamera.py
```

- If the setup is correct, the script will capture an image from your webcam and send it to the specified Telegram chat.

### Step 4: Configure Windows Task Scheduler to Run the Script Automatically

- Open Task Scheduler:

    - Press `Windows + R`, type `taskschd.msc`, and press Enter to open Task Scheduler.

- Create a New Task:

    - In the Task Scheduler window, click `Create Task` on the right-hand side.

- General Settings:

    - Give your task a name (e.g., "Telegram Photo Capture").
    - Choose "Run whether user is logged on or not" for the task to run even when you're not logged in.
    - Check the box `Run with highest privileges` to ensure the task runs without permission issues.

- Set the Trigger:

    - Click on the `Triggers` tab and click `New`.
    - Set the desired schedule (e.g., daily, weekly, or at a specific time).
    - Click `OK` when finished.

- Set the Action:

    - Go to the `Actions` tab and click `New`.
    - Choose `Start a program` as the action.
    - In the `Program/script` box, browse to the `pythonw.exe` executable (usually located in your Python installation directory, e.g., `C:\Python3x\pythonw.exe`).
    - In the `Add arguments (optional)` box, enter the following argument:

        ```bash
        "C:\path\to\your\StealthCamera.py"
        ```
    - Note: Replace `C:\path\to\your\StealthCamera.py` with the actual path to your Python script. Enclose the path in quotes if it contains spaces. Make sure that you use `pythonw.exe` (or `pyw.exe`).

- Save the Task:

    - Click `OK` to save the task.
    - If prompted, enter your Windows account password to allow the task to run with the specified privileges.

If the following instructions were followed correctly, after logging into your computer, you should receive an image from the camera.

## Troubleshooting

If you encounter any issues, consider the following troubleshooting steps:

- Ensure that your webcam is properly connected and recognized by your computer.
- Verify that the Bot Token and Chat ID in your script are correct.
- Check if the required Python libraries (`opencv-python` and `requests`) are installed correctly.
- Review the Task Scheduler settings to ensure the task is configured to run at the desired time and with the correct privileges.
- Check the Task Scheduler history for any errors or warnings related to the task execution.

If you still face issues, consult the documentation for the libraries used or seek help from the community forums.
