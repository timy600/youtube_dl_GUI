from __future__ import unicode_literals
import youtube_dl
from tkinter import *

url = "https://www.youtube.com/watch?v=kJQP7kiw5Fk"
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
"""
window = Tk()
window.wm_title("Telecharger un son Youtube")
window.mainloop()
"""
