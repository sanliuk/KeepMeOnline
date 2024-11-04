import pyautogui
import time
import threading
import customtkinter as ctk
from tkinter import messagebox

# Configura lo stile globale per customtkinter
ctk.set_appearance_mode("system")  # 'system' (default), 'dark', 'light'
ctk.set_default_color_theme("blue")  # 'blue' (default), 'dark-blue', 'green'

# Variabile globale per il controllo dello stato del movimento e della pressione di un tasto
running = False
use_key = False

def start_movement():
    global running
    if running:
        return  # Se è già in esecuzione, non fare nulla
    running = True
    start_button.configure(fg_color="green", text_color="white")
    stop_button.configure(fg_color="white", text_color="black")

    try:
        interval = float(interval_entry.get())
        distance = int(distance_entry.get())
        key_to_press = key_entry.get() if use_key else None
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for interval and distance.")
        return

    def move_mouse_and_press_key():
        while running:
            x, y = pyautogui.position()
            pyautogui.moveTo(x + distance, y)
            time.sleep(0.1)
            pyautogui.moveTo(x, y)
            if key_to_press:
                pyautogui.press(key_to_press)
            time.sleep(interval)

    threading.Thread(target=move_mouse_and_press_key, daemon=True).start()

def stop_movement():
    global running
    running = False
    start_button.configure(fg_color="white", text_color="black")
    stop_button.configure(fg_color="red", text_color="white")

def toggle_use_key():
    global use_key
    use_key = not use_key

def on_ctrl_p(event=None):
    stop_movement()

root = ctk.CTk()
root.title("Keep Me Online")
root.geometry("300x250")

interval_label = ctk.CTkLabel(root, text="Interval (seconds):")
interval_label.pack(pady=(10, 0))
interval_entry = ctk.CTkEntry(root, justify='center', width=120)
interval_entry.pack(pady=5)
interval_entry.insert(0, "300")

distance_label = ctk.CTkLabel(root, text="Distance (pixels):")
distance_label.pack(pady=(10, 0))
distance_entry = ctk.CTkEntry(root, justify='center', width=120)
distance_entry.pack(pady=5)
distance_entry.insert(0, "1")

key_label = ctk.CTkLabel(root, text="Key to press:")
key_label.pack(pady=(10, 0))
key_entry = ctk.CTkEntry(root, justify='center', width=120)
key_entry.pack(pady=5)

key_checkbox = ctk.CTkCheckBox(root, text="Use also this key:", command=toggle_use_key)
key_checkbox.pack(pady=(5, 10))

start_button = ctk.CTkButton(root, text="Start", command=start_movement, width=120, corner_radius=20)
start_button.pack(pady=(10, 5))

stop_button = ctk.CTkButton(root, text="Stop (or press Ctrl+P to stop)", command=stop_movement, width=120, corner_radius=20)
stop_button.pack(pady=(5, 10))

root.bind("<Control-p>", on_ctrl_p)
root.mainloop()
