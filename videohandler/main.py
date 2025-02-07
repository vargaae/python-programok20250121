import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from tkinter.scrolledtext import ScrolledText
import yt_dlp as youtube_dl
import csv
from PIL import Image, ImageTk
import moviepy as mp
import threading

# Konfiguráció
DARK_MODE = {
    # 'bg': '#2d2d2d',
    # 'fg': '#ffffff',
    # 'button_bg': '#3d3d3d',
    # 'button_fg': '#ffffff',
    # 'entry_bg': '#4d4d4d',
    # 'entry_fg': '#ffffff',
    # 'text_bg': '#3d3d3d',
    # 'text_fg': '#ffffff'
    'bg': '#ffffff',
    'fg': '#000000',
    'button_bg': '#f0f0f0',
    'button_fg': '#000000',
    'entry_bg': '#e0e0e0',
    'entry_fg': '#000000',
    'text_bg': '#f0f0f0',
    'text_fg': '#000000'
}

LIGHT_MODE = {
    'bg': '#ffffff',
    'fg': '#000000',
    'button_bg': '#f0f0f0',
    'button_fg': '#000000',
    'entry_bg': '#e0e0e0',
    'entry_fg': '#000000',
    'text_bg': '#f0f0f0',
    'text_fg': '#000000'
}

class VideoHandler:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("1400x800")  # Nagyobb ablak
        self.mode = DARK_MODE
        self.style = ttk.Style()
        self.apply_theme()

        self.download_thread = None
        self.downloading = False
        self.paused = False

        self.create_widgets()

    def apply_theme(self):
        self.style.configure('.', background=self.mode['bg'], foreground=self.mode['fg'])
        self.style.configure('TFrame', background=self.mode['bg'])
        self.style.configure('TLabel', background=self.mode['bg'], foreground=self.mode['fg'])
        self.style.configure('TButton', background=self.mode['button_bg'], foreground=self.mode['button_fg'])
        self.style.configure('TEntry', background=self.mode['entry_bg'], foreground=self.mode['entry_fg'])
        self.style.configure('TProgressbar', background=self.mode['button_bg'])

        self.root.config(bg=self.mode['bg'])
        for widget in self.root.winfo_children():
            if widget.winfo_class() not in ['TFrame', 'TLabel', 'TButton', 'TEntry', 'TProgressbar']:
                widget.config(bg=self.mode['bg'], fg=self.mode['fg'])

    def create_widgets(self):
        # Bal harmad: Videó- és zenelejátszó
        self.left_frame = ttk.Frame(self.root, width=400)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.player_label = ttk.Label(self.left_frame, text="Videó- és zenelejátszó")
        self.player_label.pack(pady=10)

        self.playlist = ScrolledText(self.left_frame, height=20, width=50)
        self.playlist.pack(pady=10)

        self.play_button = ttk.Button(self.left_frame, text="Lejátszás", command=self.play_media)
        self.play_button.pack(pady=10)

        # Középső harmad: Videolejátszó
        self.middle_frame = ttk.Frame(self.root, width=400)
        self.middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.video_label = ttk.Label(self.middle_frame, text="Videolejátszó")
        self.video_label.pack(pady=10)

        self.video_canvas = tk.Canvas(self.middle_frame, bg='black', width=320, height=240)
        self.video_canvas.pack(pady=10)

        self.fullscreen_button = ttk.Button(self.middle_frame, text="Teljes képernyő", command=self.toggle_fullscreen)
        self.fullscreen_button.pack(pady=10)

        # Jobb harmad: Videó- és zeneletöltő
        self.right_frame = ttk.Frame(self.root, width=400)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.download_label = ttk.Label(self.right_frame, text="Videó- és zeneletöltő")
        self.download_label.pack(pady=10)

        self.url_entry = ttk.Entry(self.right_frame, width=50)
        self.url_entry.pack(pady=10)

        self.quality_var = tk.StringVar(value='best')
        self.quality_menu = ttk.Combobox(self.right_frame, textvariable=self.quality_var, values=['best', '360p', '720p', '1080p'])
        self.quality_menu.pack(pady=10)

        self.format_var = tk.StringVar(value='mp4')
        self.format_menu = ttk.Combobox(self.right_frame, textvariable=self.format_var, values=['mp4', 'mp3', 'flac'])
        self.format_menu.pack(pady=10)

        self.download_button = ttk.Button(self.right_frame, text="Letöltés", command=self.start_download)
        self.download_button.pack(pady=10)

        self.pause_button = ttk.Button(self.right_frame, text="Szüneteltetés", command=self.toggle_pause)
        self.pause_button.pack(pady=10)

        self.cancel_button = ttk.Button(self.right_frame, text="Megszakítás", command=self.cancel_download)
        self.cancel_button.pack(pady=10)

        self.progress_label = ttk.Label(self.right_frame, text="Letöltési állapot:")
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.right_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress_bar.pack(pady=10)

        self.log_text = ScrolledText(self.right_frame, height=10, width=50)
        self.log_text.pack(pady=10)

        # Módváltó gomb
        self.mode_button = ttk.Button(self.root, text="Dark/Light Mode", command=self.toggle_mode)
        self.mode_button.pack(side=tk.BOTTOM, pady=10)

    def toggle_mode(self):
        self.mode = LIGHT_MODE if self.mode == DARK_MODE else DARK_MODE
        self.apply_theme()

    def play_media(self):
        # Ide jön a média lejátszásának implementációja
        pass
    # TODO: implement:
        # selected_item = self.video_list.selection()
        # if not selected_item:
        #     messagebox.showerror("Error", "No video selected")
        #     return

        # index = self.video_list.index(selected_item[0])
        # video = self.video_data[index]

        # try:
        #     media = self.vlc_instance.media_new(video["Path"])
        #     self.media_player.set_media(media)
        #     self.media_player.play()
        #     self.update_seek_slider()
        # except Exception as e:
        #     messagebox.showerror("Error", f"Could not play video: {e}")

    def toggle_fullscreen(self):
        # Ide jön a teljes képernyős mód implementációja
        pass

    def start_download(self):
        urls = self.url_entry.get().split()
        if not urls:
            messagebox.showerror("Hiba", "Kérjük, adjon meg egy YouTube linket!")
            return

        self.downloading = True
        self.paused = False
        self.progress_bar['value'] = 0
        self.log_text.delete(1.0, tk.END)

        self.download_thread = threading.Thread(target=self.download_media, args=(urls,))
        self.download_thread.start()

    def download_media(self, urls):
        options = {
            'format': self.quality_var.get() if self.format_var.get() == 'mp4' else 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.format_var.get(),
                'preferredquality': '192' if self.format_var.get() == 'mp3' else '0',
            }] if self.format_var.get() in ['mp3', 'flac'] else [],
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            for url in urls:
                if not self.downloading:
                    break
                ydl.download([url])

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent_str = d['_percent_str'].strip('%').strip()
            try:
                percent = float(percent_str)
            except ValueError:
                percent = 0.0

            self.progress_bar['value'] = percent
            self.progress_label.config(text=f"Letöltés: {d['_percent_str']}")
            self.log_text.insert(tk.END, f"{d['filename']} - {d['_percent_str']}\n")
            self.log_text.yview(tk.END)

    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_button.config(text="Folytatás" if self.paused else "Szüneteltetés")

    def cancel_download(self):
        self.downloading = False
        self.progress_label.config(text="Letöltés megszakítva")
        self.log_text.insert(tk.END, "Letöltés megszakítva\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoHandler(root)
    root.mainloop()