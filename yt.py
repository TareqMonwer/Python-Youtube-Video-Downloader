'''
import pytube
print("Enter the video link")
link = input()

yt = pytube.YouTube(link)

stream = yt.streams.first()



print("You file will be saved in Downloads")
destination = '/home/tareq/Downloads'
stream.download(destination)

print("\nVideo has been downloaded")
'''

from tkinter import *
from tkinter import ttk
import pytube


# Functions

def dload():
    try:
        link = link_txt.get()
        yt = pytube.YouTube(link)
        stream = yt.streams.first()
        destination = '/home/tareq/Downloads'
        stream.download(destination)
        print("Downloading")
    except:
        print("something is wrong")
    
    


window = Tk()

# Labels
l1 = Label(window, text="Video Link")
l1.grid(row=0, column=0)


# Entry
link_txt = StringVar()
e1 = Entry(window, textvariable=link_txt)
e1.grid(row=0, column=1)

# Button
b1 = Button(window, text="Download", command=dload)
b1.grid(row=0, column=2)

# Seperator
s1 = ttk.Separator(window, orient=HORIZONTAL,).grid(row=2, columnspan=5, sticky="ew")

# Text
txt1 = Text(window, height=2, width=40, fg='red')
txt1.grid(row=3, columnspan=5)
txt1.insert(END, "Your file will be saved in Downloads\nThanks for using my tool\n")
txt1.configure(state="disabled")

stat = StringVar()
txt2 = Text(window, height=2, width=40, fg='green')
txt2.grid(row=4, columnspan=5)
txt2.insert(END, stat)







window.mainloop()















