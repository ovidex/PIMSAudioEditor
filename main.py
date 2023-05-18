import tkinter as tk
from tkinter import filedialog
import pygame


class AudioPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio Player")
        self.geometry("400x200")

        self.file_path = ""
        self.is_playing = False
        self.is_paused = False

        self.file_label = tk.Label(self, text="No file selected")
        self.file_label.pack(pady=10)

        self.open_button = tk.Button(self, text="Open", command=self.open_file)
        self.open_button.pack()

        self.play_button = tk.Button(self, text="Play", command=self.play_pause_song, state=tk.DISABLED)
        self.play_button.pack()

        self.volume_label = tk.Label(self, text="Volume")
        self.volume_label.pack()

        self.volume_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.adjust_volume)
        self.volume_slider.set(100);
        self.volume_slider.pack()

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if self.file_path:
            self.file_label.config(text="Selected file: " + self.file_path)
            self.play_button.config(state=tk.NORMAL)
        else:
            self.file_label.config(text="No file selected")
            self.play_button.config(state=tk.DISABLED)

    def play_pause_song(self):
        if self.file_path:
            if not self.is_playing:
                pygame.mixer.init()
                pygame.mixer.music.load(self.file_path)
                pygame.mixer.music.set_volume(self.volume_slider.get() / 100)
                pygame.mixer.music.play()
                self.is_playing = True
                self.play_button.config(text="Pause")
            else:
                if not self.is_paused:
                    pygame.mixer.music.pause()
                    self.is_paused = True
                    self.play_button.config(text="Unpause")
                else:
                    pygame.mixer.music.unpause()
                    self.is_paused = False
                    self.play_button.config(text="Pause")

    def adjust_volume(self, volume):
        if self.is_playing:
            pygame.mixer.music.set_volume(int(volume) / 100)

    def quit(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        self.destroy()


if __name__ == "__main__":
    app = AudioPlayerApp()
    app.mainloop()
