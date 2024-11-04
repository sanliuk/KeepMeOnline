import pyautogui
import time
import threading
import customtkinter as ctk
from tkinter import messagebox

# Variabile globale per il controllo dello stato del movimento
running = False

# Funzione per avviare il movimento del mouse
def start_movement():
    global running
    if running:
        return  # Se è già in esecuzione, non fare nulla
    running = True
    start_button.configure(fg_color="green", text_color="white")  # Verde con testo bianco per Start
    stop_button.configure(fg_color="white", text_color="black")  # Bianco con testo nero per Stop

    # Legge i valori di intervallo e distanza dalla GUI
    try:
        interval = float(interval_entry.get())
        distance = int(distance_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for interval and distance.")
        return

    # Funzione che esegue il movimento del mouse in un thread separato
    def move_mouse():
        while running:
            x, y = pyautogui.position()
            pyautogui.moveTo(x + distance, y)
            time.sleep(0.1)
            pyautogui.moveTo(x, y)
            time.sleep(interval)

    # Avvia il movimento del mouse in un thread separato per non bloccare la GUI
    threading.Thread(target=move_mouse, daemon=True).start()

# Funzione per fermare il movimento del mouse
def stop_movement():
    global running
    running = False
    start_button.configure(fg_color="white", text_color="black")  # Bianco con testo nero per Start
    stop_button.configure(fg_color="red", text_color="white")  # Rosso con testo bianco per Stop

# Funzione per interrompere il movimento con Ctrl+P
def on_ctrl_p(event=None):
    stop_movement()

# Configurazione di `customtkinter`
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Creazione dell'interfaccia GUI con customtkinter
root = ctk.CTk()
root.title("Keep Me Onlin")
root.geometry("300x250")

# Label e Entry per l'intervallo di movimento
interval_label = ctk.CTkLabel(root, text="Interval (seconds):")
interval_label.pack(pady=(10, 0))
interval_entry = ctk.CTkEntry(root, justify='center', width=120)
interval_entry.pack(pady=5)
interval_entry.insert(0, "300")  # Valore predefinito

# Imposta l'icona della finestra (assicurati che il percorso dell'icona sia corretto)
root.iconbitmap("favicon.ico")

# Label e Entry per la distanza di movimento
distance_label = ctk.CTkLabel(root, text="Distance (pixels):")
distance_label.pack(pady=(10, 0))
distance_entry = ctk.CTkEntry(root, justify='center', width=120)
distance_entry.pack(pady=5)
distance_entry.insert(0, "1")  # Valore predefinito

# Bottone Start
start_button = ctk.CTkButton(root, text="Start", command=start_movement, width=120, corner_radius=20)
start_button.pack(pady=(10, 5))

# Bottone Stop con Ctrl+P indicato
stop_button = ctk.CTkButton(root, text="Stop (or press Ctrl+P to stop)", command=stop_movement, width=120, corner_radius=20)
stop_button.pack(pady=(5, 10))

# Binding globale per fermare il movimento con Ctrl+P
root.bind("<Control-p>", on_ctrl_p)

# Avvia la finestra GUI
root.mainloop()
