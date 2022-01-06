#cSpell:ignore pygame chdir

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


def getFiles():
    musicFilesDirectory = askdirectory()
    os.chdir(musicFilesDirectory)  # change dir to path
    return [f for f in os.listdir() if f.endswith(".mp3")]


def makeButton(txt, action) -> tkr.Button:
    return tkr.Button(musicPlayer,
                      width=5,
                      height=3,
                      font="Helvetica 14 bold",
                      bg="red",
                      fg="white",
                      text=txt,
                      command=action)


if __name__ == "__main__":
    musicPlayer = tkr.Tk()
    musicPlayer.title("Music Player")
    musicPlayer.geometry("450x350")  #no spaces

    songlist = getFiles()

    playList = tkr.Listbox(
        musicPlayer,
        font="Helvetica 12 bold",
        bg="yellow",
        selectmode=tkr.SINGLE)  #using css style for the font

    for item in songlist:
        playList.insert(0, item)

    pygame.init()
    pygame.mixer.init()

    def play():
        pygame.mixer.music.load(playList.get(tkr.ACTIVE))
        songTitle.set(playList.get(tkr.ACTIVE))
        pygame.mixer.music.play()

    def pause():
        pygame.mixer.music.pause()

    def unpause():
        pygame.mixer.music.unpause()

    def exitMusicPlayer():
        pygame.mixer.music.stop()

    buttonPlay = makeButton("play".upper(), play)
    buttonPause = makeButton("pause".upper(), pause)
    buttonUnpause = makeButton("unpause".upper(), unpause)
    buttonStop = makeButton("stop".upper(), exitMusicPlayer)

    songTitle = tkr.StringVar()
    currentSongDisplay = tkr.Label(musicPlayer,
                                   font="Helvetica 16 bold",
                                   textvariable=songTitle)

    currentSongDisplay.pack()
    buttonPlay.pack(fill="x")
    buttonPause.pack(fill="x")
    buttonUnpause.pack(fill="x")
    buttonStop.pack(fill="x")

    playList.pack(fill="both", expand="yes")

    musicPlayer.mainloop()
