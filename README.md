Keep Me Online



Overview

Keep Me Online is a simple Python-based UI application that prevents online inactivity detection by simulating user inputs. The tool can periodically move the mouse cursor or send a keyboard input (such as pressing the Shift key) to keep the user appearing active in online sessions.

Features

Customizable Activity Simulation:

Set the mouse movement distance (default: 50 px).

Choose the interval between actions (default: 50 seconds).

Select a keyboard input to simulate (default: Shift).

Start/Stop Functionality:

Press the Start button to activate the "Keep Me Online" process.

Press the Stop button to end the process.

Status Indicator:

Green status when active.

Red status when inactive.

Emergency Stop:

Press Ctrl + P to immediately terminate the process.

Installation

Prerequisites

Python 3.x

Required libraries: pyautogui, tkinter

Setup

Clone the repository:

git clone https://github.com/yourusername/keep-me-online.git
cd keep-me-online

Install dependencies:

pip install -r requirements.txt

Run the application:

python keep_me_online.py

Usage

Launch the script.

Configure movement distance, loop interval, and input key.

Click Start to begin simulating user activity.

Click Stop to halt the process.

Use Ctrl + P for an emergency stop.

Disclaimer

This tool is intended for ethical use only. The author is not responsible for any misuse or consequences arising from its application.

License

MIT License

