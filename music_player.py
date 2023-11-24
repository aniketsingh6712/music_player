from tkinter import *
from PIL import Image,ImageTk
import random
import os
import pygame
import time
root=Tk()
root.geometry("300x570")
import math
import multiprocessing
import time
from mutagen.mp3 import MP3

folder_path=r"D:\Music" # folder path containing music files
songs=os.listdir(folder_path)
#required variables 
c=1
current_song=0

def play_time():
    current_time=pygame.mixer.music.get_pos() /1000
    converted_current_time=time.strftime('%M:%S',time.gmtime(current_time))
    song_mut=MP3(folder_path+"/"+songs[current_song])
    global song_length
    song_length=song_mut.info.length
    #convert to time format
    converted_song_length=time.strftime('%M:%S',time.gmtime(song_length))
    #outptuing status bar
    status_bar.config(text=f'Time Elapsed:{converted_current_time} of {converted_song_length}')
    if converted_song_length==converted_current_time:
        change()
        play_next_song()
        
    status_bar.after(1000,play_time)
def random_bg_color() :
    colors=["#421AFF","#36D4D9","#69D990","#D93859","#D9866D","#AFD9D5","#75FA8D","#7F82BB","#377E47","#EA3680","#C6EAE6"]
    color=random.choice(colors)
    return color

def change():
    global c
    pause= PhotoImage(file=r"C:\Users\hp\Downloads\icons8-pause-50.png")
    play= PhotoImage(file=r"C:\Users\hp\Downloads\icons8-play-50.png")
    img=pause if c==0 else play
    if c==0:
        unpause_music()
    else:
        pause_music()
    c=1 if c==0 else 0
    icon_button1.config(image=img)
    icon_button1.image=img


#changing top text
def change_text():
    global current_song
    a=top(current_song+1,len(songs))
    tp.config(text=a)
    
    
def top(a,b):
    return r"Playing %d of %d"%(a,b)

# fn for song name
def songname():
    global current_song
    song_name,file_extension=os.path.splitext(songs[current_song])
    return song_name
def change_song_name():
    song=songname()
    song_name.config(text=song.upper())
# Function to play the current song

    
# Function to play the next song
def play_next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    pygame.mixer.music.load(folder_path+"/"+songs[current_song])
    change_text()
    change_song_name()
    play_current_song()
    
def play_prev_song():
    global current_song
    
    current_song = (current_song -1) % len(songs)
    pygame.mixer.music.load(folder_path+"/"+songs[current_song])
    change_text()
    change_song_name()
    play_current_song()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()
    root.destroy()

def change_vol(value):
    volume=int(float(value))/10
    pygame.mixer.music.set_volume(volume)
def play_current_song():
    global c
   
    bgc=random_bg_color()
    root.config(bg=bgc)
    song_name.config(bg=bgc)
    tp.config(bg=bgc)
    status_bar.config(bg=bgc)
    
    pygame.mixer.music.play(loops=0)
    if c==1:
        pygame.mixer.music.unpause()
    if c==0:
        pygame.mixer.music.pause()
    play_time()


pygame.init()
pygame.mixer.music.load(folder_path+"/"+songs[current_song])


a=top(current_song+1,len(songs))
tp=Label(root,text=a,fg="black",font="time 10 bold")
x=(root.winfo_reqwidth()-tp.winfo_reqwidth())/2
tp.place(x=x+30,y=20)

#image
image=Image.open(r"C:\Users\hp\Downloads\music-pl.jpeg")
image=image.resize((200,200))
test=ImageTk.PhotoImage(image)
note_label=Label(image=test)
x=(root.winfo_reqwidth()-tp.winfo_reqwidth())/2
note_label.place(x=x,y=50)

#button play/pause
play= PhotoImage(file=r"C:\Users\hp\Downloads\icons8-pause-50.png")  #icon folder
icon_button1 =Button(root,image=play,width=40,height=40, command=change)
x=(root.winfo_reqwidth()-tp.winfo_reqwidth())/2
icon_button1.place(x=x+70,y=330)

#music name
song=songname()
song_name=Label(root,text=song.upper(),fg="black",font="Times-Roman 17 bold")
song_name.pack(expand=True, fill='both',pady=270)


#prev and next
prev = PhotoImage(file=r"C:\Users\hp\Downloads\icons8-skip-back-48.png") 
icon_button3 =Button(root, image=prev,width=40,height=40, command=play_prev_song)
icon_button3.place(x=30,y=330)

nxt= PhotoImage(file=r"C:\Users\hp\Downloads\icons8-next-48.png") 
icon_button4 =Button(root, image=nxt,width=40,height=40, command=play_next_song)
icon_button4.place(x=230,y=330)

#status bar
status_bar=Label(root,text='',fg='white',bd=1,relief=GROOVE,anchor=E,font="Times-Roman 11 bold")
status_bar.place(x=55,y=445)
# volume slider

slider=Scale(root,from_=0,to=10,orient=HORIZONTAL,command=change_vol)
slider.place(x=x+40,y=390)

volume=0.3
pygame.mixer.music.set_volume(volume)
default_value = 3
slider.set(default_value)

#status bar
status_bar=Label(root,text='',bd=1,relief=GROOVE,anchor=E,font="Times-Roman 11 bold")
status_bar.place(x=55,y=450)


#closing windows
root.protocol("WM_DELETE_WINDOW", stop_music)
#music code
play_current_song()

root.resizable(width=False, height=False)
root.mainloop()