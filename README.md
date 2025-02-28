# Keep Me Online


## Overview
**Keep Me Online** is a simple Python-based UI application that prevents online inactivity detection by simulating user inputs. The tool can periodically move the mouse cursor or send a keyboard input (such as pressing the Shift key) to keep the user appearing active in online sessions.
![Keep Me Online UI](ExeScreenshot.png)

This application is ready to use as an executable (`.exe`) and can be used by anyone without requiring installation.

## Features
- **Customizable Activity Simulation:**
  - Set the mouse movement distance (default: **50 px**).
  - Choose the interval between actions (default: **50 seconds**).
  - Select a keyboard input to simulate (default: **Shift**).
- **Start/Stop Functionality:**
  - Press the **Start** button to activate the "Keep Me Online" process.
  - Press the **Stop** button to end the process.
- **Status Indicator:**
  - Green status when active.
  - Red status when inactive.
- **Emergency Stop:**
  - Press **Ctrl + P** to immediately terminate the process.

## For Developers / Modifications
If you are interested in modifying the script, follow these steps to set up the development environment.

### Prerequisites
- Python 3.x
- Required libraries: `pyautogui`, `tkinter`

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/keep-me-online.git
   cd keep-me-online
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python keep_me_online.py
   ```

## Usage
1. Launch the executable or run the script.
2. Configure movement distance, loop interval, and input key.
3. Click **Start** to begin simulating user activity.
4. Click **Stop** to halt the process.
5. Use **Ctrl + P** for an emergency stop.

## Disclaimer
This tool is intended for ethical use only. The author is not responsible for any misuse or consequences arising from its application.

## License
[MIT License](LICENSE)
