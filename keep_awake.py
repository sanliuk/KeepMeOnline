import pyautogui
import time
import threading
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk

# Variabile globale per il controllo dello stato del movimento e della pressione di un tasto
running = False
use_key = False

# Crea la finestra principale prima della creazione delle immagini
root = ctk.CTk()
root.title("Keep Me Online")
root.geometry("350x300")

# Funzione per creare un'immagine circolare di un dato colore
def create_circle_image(color, size=(10, 10)):
    image = Image.new("RGBA", size, (255, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, size[0], size[1]), fill=color)
    return ImageTk.PhotoImage(image)

# Crea le immagini per i pallini verde e rosso dopo aver creato la finestra principale
circle_green = create_circle_image("green")
circle_red = create_circle_image("red")

def start_movement():
    global running
    if running:
        return  # Se è già in esecuzione, non fare nulla
    running = True
    update_status("activated")  # Aggiorna lo stato a attivato
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
    update_status("deactivated")  # Aggiorna lo stato a disattivato
    start_button.configure(fg_color="white", text_color="black")
    stop_button.configure(fg_color="red", text_color="white")

def toggle_use_key():
    global use_key
    use_key = not use_key

def on_ctrl_p(event=None):
    stop_movement()

def update_status(status):
    if status == "activated":
        status_label.configure(text="Status: Activated", image=circle_green, compound="left")
    elif status == "deactivated":
        status_label.configure(text="Status: Deactivated", image=circle_red, compound="left")
    else:
        status_label.configure(text="Status: None", image="", compound="left")

interval_label = ctk.CTkLabel(root, text="Interval (seconds):")
interval_label.pack(pady=(10, 0))
interval_entry = ctk.CTkEntry(root, justify='center', width=120)
interval_entry.pack(pady=5)
interval_entry.insert(0, "300")

# Imposta l'icona della finestra (assicurati che il percorso dell'icona sia corretto)
root.iconbitmap("favicon.ico")

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

status_label = ctk.CTkLabel(root, text="Status: None", image="", compound="left")  # Inizialmente senza immagine
status_label.pack(pady=(10, 0))

root.bind("<Control-p>", on_ctrl_p)

root.mainloop()
