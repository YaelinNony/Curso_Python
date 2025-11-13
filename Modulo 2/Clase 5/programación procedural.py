#Programación procedural
#Programa creado por: Mayo
# --- VERSION 1: CÓDIGO PROCEDURAL ---
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import yt_dlp as ydl
import os
import threading
import sys

# --- 1. ESTADO GLOBAL (Variables Globales) ---
# Todas nuestras "partes" viven sueltas y en el scope global.
# Cualquiera puede modificarlas por accidente.
root = tk.Tk()
root.title("Descargador Procedural")

save_path = tk.StringVar()
downloaded_count = 0
total_videos = 0

# --- 2. FUNCIONES GLOBALES ---
# Estas funciones dependen de las variables globales de arriba.

def get_ffmpeg_path():
    """Devuelve la ruta de FFmpeg en el directorio del proyecto."""
    base_path = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "ffmpeg", "ffmpeg.exe")

def get_playlist_info(url):
    """Obtiene la cantidad total de videos de una playlist."""
    global total_videos # Modifica una variable global
    try:
        ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
        with ydl.YoutubeDL(ydl_opts) as ydl_instance:
            info = ydl_instance.extract_info(url, download=False)
            total_videos = len(info["entries"]) if "entries" in info else 1
    except Exception:
        total_videos = 1
    return total_videos

# "Infierno de Parámetros": ¡Esta función necesita 6 argumentos
# solo para saber a qué widgets de la GUI debe actualizar!
def download_video(url, save_path, progress_bar, status_label, song_label, count_label):
    """Inicia el hilo de descarga."""
    if not url.strip() or not save_path.strip():
        messagebox.showerror("Error", "URL y carpeta de destino son obligatorias.")
        return
        
    # Inicia el hilo, pasando OTRA VEZ todos los widgets
    thread = threading.Thread(target=download_video_thread, 
                              args=(url, save_path, progress_bar, status_label, song_label, count_label))
    thread.start()

def download_video_thread(url, save_path, progress_bar, status_label, song_label, count_label):
    """Hilo secundario donde se ejecuta la descarga."""
    global downloaded_count, total_videos # ¡Peligroso! Modifica estado global
    
    downloaded_count = 0
    total_videos = get_playlist_info(url)
    
    # Actualiza widgets globales (pasados como parámetros)
    count_label.config(text=f"Canciones descargadas: 0 / {total_videos}")
    status_label.config(text="Descargando...")
    progress_bar["value"] = 0
    root.update_idletasks() # ¡Depende de la variable global 'root'!

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{save_path}/%(playlist_title)s/%(title)s.%(ext)s',
        # El hook está forzado a recibir todos los widgets...
        'progress_hooks': [lambda d: update_progress(d, progress_bar, status_label, song_label, count_label)],
        'ignoreerrors': True,
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        'ffmpeg_location': get_ffmpeg_path(),
    }

    try:
        with ydl.YoutubeDL(ydl_opts) as ydl_instance:
            ydl_instance.download([url])
        status_label.config(text="Descarga completa ✅")
        song_label.config(text="✔ Todas las canciones han sido descargadas")
        messagebox.showinfo("Éxito", "Descarga completa.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")
        status_label.config(text="Error ❌")

def update_progress(d, progress_bar, status_label, song_label, count_label):
    """Actualiza la GUI. Esta función es un 'callback'."""
    global downloaded_count # ¡Peligroso! Acoplamiento fuerte
    
    if d['status'] == 'downloading':
        percentage = (d.get('downloaded_bytes', 0) / d.get('total_bytes', 1)) * 100
        progress_bar["value"] = percentage
        song_name = os.path.splitext(os.path.basename(d.get('filename', '...')))[0]
        status_label.config(text=f"Descargando... {percentage:.2f}%")
        song_label.config(text=f"{song_name}")
        root.update_idletasks() # ¡Depende de la variable global 'root'!

    elif d['status'] == 'finished':
        downloaded_count += 1
        count_label.config(text=f"Canciones descargadas: {downloaded_count} / {total_videos}")
        progress_bar["value"] = 0
        root.update_idletasks()

def select_folder():
    """Actualiza la variable global 'save_path'."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_path.set(folder_selected)

# --- 3. CREACIÓN DE LA GUI (Código "Spaghetti") ---
# Creamos todos los widgets como variables globales
url_entry = tk.Entry(root, width=50)
save_path_entry = tk.Entry(root, textvariable=save_path, width=50)
progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
status_label = tk.Label(root, text="Esperando descarga...")
song_label = tk.Label(root, text="Canción actual: ---")
count_label = tk.Label(root, text="Canciones descargadas: 0 / 0")

# Colocamos todo en la ventana
tk.Label(root, text="URL del video/playlist:").pack(pady=5)
url_entry.pack(pady=5)
tk.Label(root, text="Guardar en:").pack(pady=5)
save_path_entry.pack(pady=5)
tk.Button(root, text="Seleccionar carpeta", command=select_folder).pack(pady=5)
progress_bar.pack(pady=10)
status_label.pack(pady=5)
song_label.pack(pady=5)
count_label.pack(pady=5)

# ¡"Parameter Hell"! El lambda necesita capturar y pasar 6 variables
tk.Button(root, text="Descargar y Convertir", 
          command=lambda: download_video(
              url_entry.get(), 
              save_path.get(), 
              progress_bar, 
              status_label, 
              song_label, 
              count_label
          )).pack(pady=20)

root.mainloop()