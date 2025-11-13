#Programación orientada a objetos
#Programa creado por: Mayo
# --- VERSION 2: CÓDIGO CON POO ---
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import yt_dlp as ydl
import os
import threading
import sys

# --- 1. LA CLASE (Nuestra "Caja" Organizadora) ---
class YouTubeDownloaderApp:
    
    # Guarda el estado (atributos)
    def __init__(self, root_window):
        """
        El constructor. Prepara la GUI y los atributos de estado.
        """
        self.root = root_window
        self.root.title("Descargador POO")
        
        # --- Atributos de Estado (reemplazan a 'global') ---
        self.save_path = tk.StringVar()
        self.downloaded_count = 0
        self.total_videos = 0
        
        # --- Atributos de GUI (reemplazan a 'global') ---
        # (Encapsulación: Los widgets son propiedad del objeto)
        self.url_entry = tk.Entry(self.root, width=50)
        self.save_path_entry = tk.Entry(self.root, textvariable=self.save_path, width=50)
        self.progress_bar = ttk.Progressbar(self.root, length=300, mode="determinate")
        self.status_label = tk.Label(self.root, text="Esperando descarga...")
        self.song_label = tk.Label(self.root, text="Canción actual: ---")
        self.count_label = tk.Label(self.root, text="Canciones descargadas: 0 / 0")
        
        # Llamamos al método que construye la interfaz
        self.create_widgets()
    
    @staticmethod
    def get_ffmpeg_path():
        """Devuelve la ruta de FFmpeg. Estático porque no usa 'self'."""
        base_path = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, "ffmpeg", "ffmpeg.exe")

    def create_widgets(self):
        """Crea y posiciona todos los widgets en la ventana."""
        tk.Label(self.root, text="URL del video/playlist:").pack(pady=5)
        self.url_entry.pack(pady=5)
        tk.Label(self.root, text="Guardar en:").pack(pady=5)
        self.save_path_entry.pack(pady=5)
        
        # Los 'command=' ahora apuntan a MÉTODOS de 'self'
        tk.Button(self.root, text="Seleccionar carpeta", command=self.select_folder).pack(pady=5)
        self.progress_bar.pack(pady=10)
        self.status_label.pack(pady=5)
        self.song_label.pack(pady=5)
        self.count_label.pack(pady=5)
        
        tk.Button(self.root, text="Descargar y Convertir", 
                  command=self.download_video).pack(pady=20)
        

    def select_folder(self):
        """Actualiza el atributo 'self.save_path'."""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.save_path.set(folder_selected)

    def get_playlist_info(self, url):
        """Obtiene la cantidad total de videos."""
        try:
            ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True}
            with ydl.YoutubeDL(ydl_opts) as ydl_instance:
                info = ydl_instance.extract_info(url, download=False)
                return len(info["entries"]) if "entries" in info else 1
        except Exception:
            return 1
            
    def download_video(self):
        """Inicia el hilo de descarga. No necesita parámetros."""
        url = self.url_entry.get()
        save_path = self.save_path.get()
        
        if not url.strip() or not save_path.strip():
            messagebox.showerror("Error", "URL y carpeta de destino son obligatorias.")
            return
            
        # Inicia el hilo, apuntando a un MÉTODO de 'self'
        thread = threading.Thread(target=self.download_video_thread, args=(url, save_path))
        thread.start()

    def download_video_thread(self, url, save_path):
        """Hilo secundario. Usa atributos de 'self'."""
        
        # Modifica atributos de 'self', no variables 'global'
        self.downloaded_count = 0
        self.total_videos = self.get_playlist_info(url)
        
        # Actualiza widgets de 'self'
        self.count_label.config(text=f"Canciones descargadas: 0 / {self.total_videos}")
        self.status_label.config(text="Descargando...")
        self.progress_bar["value"] = 0
        self.root.update_idletasks()

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{save_path}/%(playlist_title)s/%(title)s.%(ext)s',
            # ¡EL MEJOR CAMBIO! El hook ahora es un método limpio.
            'progress_hooks': [self.update_progress],
            'ignoreerrors': True,
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
            'ffmpeg_location': self.get_ffmpeg_path(),
        }

        try:
            with ydl.YoutubeDL(ydl_opts) as ydl_instance:
                ydl_instance.download([url])
            self.status_label.config(text="Descarga completa ✅")
            self.song_label.config(text="✔ Todas las canciones han sido descargadas")
            messagebox.showinfo("Éxito", "Descarga completa.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")
            self.status_label.config(text="Error ❌")

    def update_progress(self, d):
        """
        Actualiza la GUI. Este 'callback' solo necesita 'self' (implícito) y 'd'.
        """
        if d['status'] == 'downloading':
            percentage = (d.get('downloaded_bytes', 0) / d.get('total_bytes', 1)) * 100
            self.progress_bar["value"] = percentage
            song_name = os.path.splitext(os.path.basename(d.get('filename', '...')))[0]
            self.status_label.config(text=f"Descargando... {percentage:.2f}%")
            self.song_label.config(text=f"{song_name}")
            self.root.update_idletasks()

        elif d['status'] == 'finished':
            # Modifica el estado encapsulado
            self.downloaded_count += 1
            self.count_label.config(text=f"Canciones descargadas: {self.downloaded_count} / {self.total_videos}")
            self.progress_bar["value"] = 0
            self.root.update_idletasks()

# --- 4. EL PUNTO DE ENTRADA (Limpio y simple) ---
# Este 'if' asegura que el código solo se ejecute
# cuando corremos el script directamente.
if __name__ == "__main__":
    main_window = tk.Tk()
    
    # 1. Creamos el objeto. ¡TODA la lógica se encapsula aquí!
    app = YouTubeDownloaderApp(main_window) 
    
    # 2. Iniciamos la aplicación.
    main_window.mainloop()