Here’s the README.md file in English, organized for both users who want to run the code and those who want to modify or fork it.




# Keep Awake Script to always appear Online

This project contains a Python script to keep your Discord status active by simulating periodic mouse movements.

## 1. For Users Who Just Want to Run the Program

### Prerequisites
- **Python** 3.11.4 or higher installed on your computer.

### Steps to Run the Program

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/keep-awake.git
   cd keep-awake


2.Install Dependencies: Install pyautogui, which is required for mouse control:



pip install pyautogui

3.Create an Executable with pyinstaller (Optional): If you want to create an .exe file, install pyinstaller and run the command below:

python -m pip install --user pyinstaller
C:\Users\[your_name]\AppData\Roaming\Python\Python311\Scripts\pyinstaller --onefile keep_awake.py


You’ll find the .exe file in the dist folder, ready to run with a double-click.

Note: If pyinstaller is not recognized, add the scripts folder (C:\Users\[your_name]\AppData\Roaming\Python\Python311\Scripts) to your system PATH.


2. For Users Who Want to Modify or Fork the Code
If you want to customize the script, here are the key files and commands to work with the code.

Project Structure
keep_awake.py: The main file containing the code to keep your Discord status active.
Steps to Modify
Edit the Code: Open keep_awake.py in an editor like Visual Studio Code, and customize the behavior. For example, you can modify time.sleep(300) to change how often the mouse moves (300 seconds = 5 minutes).

Run the Script to Test:
python keep_awake.py
Create an Executable for Distribution: After making modifications, create a new .exe by running:
C:\Users\[your_name]\AppData\Roaming\Python\Python311\Scripts\pyinstaller --onefile keep_awake.py


The updated executable will appear in the dist folder.

Troubleshooting
pyinstaller not recognized: Add the path C:\Users\[your_name]\AppData\Roaming\Python\Python311\Scripts to your system PATH.
Permission error when installing packages: Use the --user flag to install packages for the current user only.


License
This project is free to use and modify for personal or educational purposes.




