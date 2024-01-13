import customtkinter
import time
import tkinter as tk
import vlc
from tkinter import ttk
import threading
import requests
import os
import pytube
from pytube import YouTube
from tkinter.ttk import *
from customtkinter import *
from PIL import Image

zielordner = ''
dateiname = 'test'
titel = ''
play_dark = Image.open('imges/dark_play_icon.png')
play_light = Image.open('imges/light_play_icon.png')
dark_stop = Image.open('imges/dark_stop_icon.png')
light_stop = Image.open('imges/light_stop_icon.png')
def open_new_window():
    # Verstecke das Hauptfenster
    root.withdraw()

    # Funktion, um das Hauptfenster wieder anzuzeigen, wenn das neue Fenster geschlossen wird
    def on_new_window_close():
        url = url_entry.get()
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(zielordner)
        root.deiconify()
        new_window.destroy()
        global titel
        titel = yt.title + '.mp4'
        time.sleep(10)
        media = vlc_instance.media_new(titel)  # Pfad zum Video angeben
        player.set_media(media)


    root.withdraw()

    # Erstellen eines neuen Fensters
    new_window = tk.Toplevel()
    new_window.title("URL Eingabe")
    new_window.geometry('600x180')
    new_window.protocol("WM_DELETE_WINDOW", on_new_window_close)

    # Hinzufügen von Widgets zum neuen Fenster

    # Label für die URL
    url_label = tk.Label(new_window, text='URL:')
    url_label.pack(side='left', fill='none')

    # Entry-Widget für die URL-Eingabe
    url_entry = tk.Entry(new_window)
    url_entry.pack(side='left', padx=10, fill="x", expand=True)

    # Button zum Schließen des Fensters
    close_button = tk.Button(new_window, text="Enter", command=on_new_window_close)
    close_button.pack(side='right')

# Hauptfenster erstellen
root = ctk_tk.CTk()
root.title("Custom Layout with VLC Player")
style = Style()
style.configure('Botoms',bg='black', fg='with', borderweight=0)
# Fenstergrstyle.configureöße auf 1920x1080 setzen
root.geometry('1920x1080')
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# Linker Bereich für den VLC-Player
left_frame_width = 1300 # Ein Drittel der Bildschirmbreite
left_frame = tk.Frame(root, bg='grey', width=left_frame_width, )
left_frame.pack(side='left', fill='both', expand=True)

# Rechter Bereich (oben und unten)
right_frame = tk.Frame(root, bg='white')
right_frame.pack(side='right', fill='both', expand=True)

# Rechter oberer Bereich
top_right_frame_height = 1080 // 2  # Die Hälfte der Bildschirmhöhe
top_right_frame_weight = 620
top_right_frame = tk.Frame(right_frame, bg='blue', height=top_right_frame_height, width=top_right_frame_weight)
top_right_frame.pack(side='top', fill='x', expand=False)

# Rechter unterer Bereich
bottom_right_frame = tk.Frame(right_frame, bg='green', width=top_right_frame_weight)
bottom_right_frame.pack(side='bottom', fill='both', expand=True)

# VLC-Player Instanz erstellen
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

# VLC-Player in den Frame einbetten
video_frame = tk.Frame(left_frame, bg='black')
video_frame.pack(side='top', fill='both', expand=True)

# Canvas für den VLC-Player
canvas = tk.Canvas(video_frame, bg='black')
canvas.pack(side='top', fill='both', expand=True)

# Nachdem das Hauptfenster angezeigt wird, die VLC-Player-Anzeige aktualisieren
def setup_player():
    video_id = canvas.winfo_id()
    player.set_hwnd(video_id)

root.after(1000, setup_player)  # Warten, bis das Tkinter-Fenster initialisiert ist

# Video laden



controls_frame = tk.Frame(left_frame, bg='black')
controls_frame.pack(side='bottom', fill='x')

# Kontrollbuttons im Container zentrieren
def skip(value):
    player.set_time(player.get_time() + value)

print(titel)

stop_button = customtkinter.CTkButton(master=controls_frame, text="", command=player.stop, font=CTkFont(size=15, family='Arial', ), corner_radius=32, fg_color='transparent', border_color="#c20000", border_width=2, image=CTkImage(light_image=light_stop,dark_image=dark_stop))
stop_button.pack(side='left', padx=(root.winfo_screenwidth()//25, 10), anchor='center')

play_button = customtkinter.CTkButton(controls_frame, text="", command=player.play, font=CTkFont(size=15, family='Arial', ), corner_radius=32, fg_color='transparent', image=CTkImage(dark_image=play_dark,light_image=play_light))
play_button.pack(side='left', padx=10, anchor='center')

pause_button = customtkinter.CTkButton(controls_frame, text="Pause", command=player.pause, font=CTkFont(size=15, family='Arial', ), corner_radius=32, fg_color='transparent')
pause_button.pack(side='left', padx=10, anchor='center')

skip_back_button = customtkinter.CTkButton(controls_frame, text="Zurück", command=lambda: skip(-1000), font=CTkFont(size=15, family='Arial', ), corner_radius=32, fg_color='transparent')
skip_back_button.pack(side='left', padx=10, anchor='center')

skip_forward_button = customtkinter.CTkButton(controls_frame, text="Vor", command=lambda: skip(1000), font=CTkFont(size=15, family='Arial', ), corner_radius=32, fg_color='transparent')
skip_forward_button.pack(side='left', padx=10, anchor='center')

URL_button = customtkinter.CTkButton(controls_frame, text="URL", command=open_new_window, font=CTkFont(size=15, family='Arial', ), corner_radius=32, fg_color='transparent')
URL_button.pack(side='left', padx=10, anchor='center')

# Hauptloop starten
root.mainloop()
