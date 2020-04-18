from __future__ import unicode_literals
import youtube_dl
from tkinter import *

"""
url = "https://www.youtube.com/watch?v=kJQP7kiw5Fk"
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
"""


window = Tk()
window.wm_title("Telecharger un son Youtube")

""" Functions"""
videos = []

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
    for ylink in videos:
        url = ylink
        print(url)

"""Value Entry"""
l1 = Label(window, text ="Lien Youtube", width = 16)
l1.grid(row = 0, column = 1)

l2 = Label(window, text ="Titre Youtube", width = 16)
l2.grid(row = 1, column = 1)
"""
l3 = Label(window, text ="Artiste", width = 16)
l3.grid(row = 2, column = 1)

l4 = Label(window, text ="Titre", width = 16)
l4.grid(row = 3, column = 1)
"""
link_text = StringVar()
e1 = Entry(window, width = 45, textvariable = link_text)
e1.grid(row = 0, column = 2, columnspan = 3)

t1 = Text(window, height = 1, width = 34)
t1.grid(row = 1, column = 2, columnspan = 3)
"""
artist_text = StringVar()
e2 = Entry(window, width = 45, textvariable = artist_text)
e2.grid(row = 2, column = 2, columnspan = 3)

title_text = StringVar()
e2 = Entry(window, width = 45, textvariable = title_text)
e2.grid(row = 3, column = 2, columnspan = 3)
"""

"""ListBox & Scrollbar"""
list1 = Listbox(window, height = 10, width = 50)
list1.grid(row = 6, column = 1, rowspan = 6, columnspan = 4)

sb1 = Scrollbar(window)
sb1.grid(row = 6, column = 4, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command= list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

"""Buttons"""
b1 = Button(window, text = "Ajouter", width=12, command = add_command)
b1.grid(row = 4, column = 1)

b2 = Button(window, text = "Telecharger", width=12, command = download_command)
b2.grid(row = 4, column = 2)

b3 = Button(window, text = "Reinitialiser", width=12, command = reinitialize_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Fermer", width=12, command = window.destroy)
b4.grid(row = 12, column = 2)

window.mainloop()
