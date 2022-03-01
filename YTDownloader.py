import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox
import ssl
# Label is a tkinter method Widget
# Entry is a tkinter method Widget
# StringVar() is a tkinter Class
# .grid() is a tkinter method geometry manager that allows you to set the parent widgets in a table like structure
# Button is a tkinter method Widget
# The Entry() point is Python & Tkinter is like 'Text Area' in html
# command= is the action keyword that activates the/a backend process

# Frontend
def createWidgets():
    #Label
    youTube_Link_Label = Label(root, text="YouTube URL: ",bg="#c31432")
    youTube_Link_Label.grid(row=1, column=0, pady=5, padx=5)
    #Entry
    root.link_text = Entry(root, width=60, textvariable=video_Link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)
    #Label
    urlLanding_label = Label(root, text="Folder: ", bg="#dd1818")
    urlLanding_label.grid(row=2,column=0,pady=5, padx=5)
    #Entry
    root.urlLanding_text = Entry(root, width=45, textvariable=download_Path_Dir)
    root.urlLanding_text.grid(row=2, column=1, pady=3, padx=3)
    #Button1
    browse_btn = Button(root, text="Browse", command=browse,width=10, bg="#240b36")
    browse_btn.grid(row=2, column=2, pady=1, padx=1)
    #Button2 
    download_btn = Button(root, text="Download Now", command=download_Video, width=25, bg="#240b36")
    download_btn.grid(row=3, column=1, pady=3, padx=3)
    
# Backend Functionality
# Functionality for the browse button which opens up the mac finder in mac to allow you to access your list of folders. (Backend functionality with filedialog)
def browse():
    #Set variable and set it = to the filedialog method keyword. Using dot notation, call the askdirectory method from the filedialog library
    download_dir_path = filedialog.askdirectory(initialdir="your dir path")

    download_Path_Dir.set(download_dir_path) 

def download_Video():
    url = video_Link.get()
    folder = download_Path_Dir.get()
    get_Video = YouTube(url)
    get_Stream = get_Video.streams.first()
    get_Stream.download(folder)
    messagebox.showinfo("Download Successful ", " Video found at" + folder)
# padx= and pady= are calculated in pixels
# This creates the window/Screen 
# Calling Geometry and setting the dimensions
root = tk.Tk()
root.geometry("800x120")
# Resizable() takes the y-axis index and the x-axis index
root.resizable(False,False)
root.title("Youtube Downloader")
root.config(background="#000000")
ssl._create_default_https_context = ssl._create_unverified_context
video_Link = StringVar()
# video_Link
download_Path_Dir = StringVar()
createWidgets()
root.mainloop()    