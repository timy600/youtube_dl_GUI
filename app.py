from __future__ import unicode_literals
import youtube_dl
from tkinter import *
#from urllib import HTTPError
window = Tk()

# style
window.wm_title("Telecharger un son Youtube")
background_color = "#1460a8"
buttons_color = "#1c79d1"
foreground_color = "#e2eaf1"
light_color = "#74abda"

#window.geometry('600x400')
window.configure(bg=background_color)
#window.configure(fg=foreground_color)
#window.background("blue")
#Functions
videos = []

# creating an output object that we will be able to manage

# GET THE OUTPUT:
# loader
# title + name, artiste, time, quality, type....



"""
class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
"""
def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
    except IndexError:
        pass

def add_command():
    videos.append(link_text.get())#, artist_text.get(),title_text.get())
    list1.delete(0,END)
    for video in videos:
        list1.insert(END, video)

def reinitialize_command():
    del videos[:]
    list1.delete(0,END)


def download_command():
    ydl_opts = {}
    for ylink in videos:
        url = ylink
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(url)
        """
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(url)
        except HTTPError as e:
            if e.code == 403:
                print("ERROR 403")
        """

        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        """




#Value Entry
l1 = Label(window, text ="Lien Youtube", width = 16, bg=background_color, foreground=foreground_color)
l1.grid(row = 0, column = 1)

l2 = Label(window, text ="Titre Youtube", width = 16, bg=background_color, foreground=foreground_color)
l2.grid(row = 1, column = 1)

link_text = StringVar()
e1 = Entry(window, width = 45, textvariable = link_text, bg=light_color)
e1.grid(row = 0, column = 2, columnspan = 3)

t1 = Text(window, height = 1, width = 34,  bg=light_color)
t1.grid(row = 1, column = 2, columnspan = 3)

#ListBox & Scrollbar
list1 = Listbox(window, height = 10, width = 50, bg=light_color)
list1.grid(row = 6, column = 1, rowspan = 6, columnspan = 4)

sb1 = Scrollbar(window, bg=light_color)
sb1.grid(row = 6, column = 4, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command= list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#Buttons
b1 = Button(window, text = "Ajouter", width=12, command = add_command,  bg=buttons_color)
b1.grid(row = 4, column = 1)

b2 = Button(window, text = "Telecharger", width=12, command = download_command, bg=buttons_color)
b2.grid(row = 4, column = 2)

b3 = Button(window, text = "Reinitialiser", width=12, command = reinitialize_command, bg=buttons_color)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Fermer", width=12, command = window.destroy, bg=buttons_color)
b4.grid(row = 12, column = 2)

window.mainloop()
