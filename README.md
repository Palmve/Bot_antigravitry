# 🤖 Auto-Management Monitor Pro (Bot Antigravity)

This bot is a visual recognition-based automation system. It is designed to monitor the screen and react to specific buttons or perform automatic scrolls if no activity is detected.

## 🚀 Prerequisites

For the bot to function correctly, you need to have:
- **Python 3.10 or higher** installed (It is recommended to check the "Add Python to PATH" option during installation).

## 🛠️ Quick Installation

1.  **Download the project** to a folder of your choice.
2.  **Run the launcher**: Double-click on the `INICIAR_MOLTBOT.bat` file.
    -   The first time, the system will automatically create a virtual environment (`.venv`) and install the necessary libraries (`pyautogui`, `Pillow`, `opencv-python`).
    -   For subsequent runs, the bot will start directly.

## 🕹️ How to use the Bot

1.  Open the application or web page you want to monitor.
2.  Launch `INICIAR_MOLTBOT.bat`.
3.  Press the **"TURN ON BOT"** button on the interface.
4.  **Bot Actions:**
    -   **Step 1 (Run):** Searches for the blue button (based on `run_button.png`). If found, it clicks and waits 5 seconds.
    -   **Step 1.5 (Expand):** Searches for the "Expand" button (based on `Expand.png`). If found, it clicks to enlarge the view.
    -   **Step 2 (Arrow):** If it doesn't see the "Run" or "Expand" buttons, it searches for a down arrow (`down_arrow.png`). If found, it clicks to scroll the screen.
    -   **Step 2.5 (Accept all):** Every 2 cycles, the bot checks if the "Accept all" button (`Accept_all.png`) is present and clicks it if necessary.
    -   **Step 3 (Auto-Scroll):** If after 2 cycles it finds nothing, the bot will perform an automatic scroll down to try and locate elements.

## 📁 Important Files

-   `Boton_Run.py`: Main bot code (Logic and GUI).
-   `INICIAR_MOLTBOT.bat`: Launcher that prepares the environment and starts the bot.
-   `requirements.txt`: List of necessary libraries.
-   `Expand.png`: Image for the view extension button.
-   `Accept_all.png`: Image to confirm acceptance messages.
-   `run_button.png` and `down_arrow.png`: Used for visual recognition.

## ⚠️ Important Notes

-   **Resolution**: The bot relies on the provided images. If the buttons on your screen look very different from the original captures, you may need to update the images in the project folder.
-   **Security**: You can stop the bot at any time by pressing the **"STOP THE BOT"** button on the interface.
-   **WARNING**: Always remember to turn off the bot when you are no longer using it. Since it performs automated scrolls and clicks, it could interfere with other open windows if left active in the background.

---
*Developed for workflow optimization.*
